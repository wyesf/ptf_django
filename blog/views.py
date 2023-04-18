from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category, Tag, Comment
from .forms import CommentForm
from .forms import PostForm
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.utils.text import slugify

# Create your views here.

# post_list
# CBV
class PostList(ListView) :
    model = Post
    # template_name = 'blog/post_list.html'
    # post_list.html : class이름_list.html 파일명을 규칙대로 바꾸면 내부적으로 정의되어 있기 때문에 생략 가능. 파일명을 위에 있는 규칙으로 하지 않을 경우 명시해줘야 함.
    ordering = '-pk'
    paginate_by = 3  #한 페이지당 보여줄 포스트 개수 정하기

    def get_context_data(self, **kwargs) :
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        # Post 테이블에서 category가 필드를 선택하지 않은 포스트의 개수
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context





# 방법2 - 딕셔너리 데이터를 변수에 바로 넣어서 사용(책341p)
def category_page(request, slug) :

    if slug == 'no_category' :
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        # 선택한 슬러그에 해당하는 Category 테이블의 레코드
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {  
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        }
    )




# detail_page
# CBV
class PostDetail(DetailView) :
    model = Post

    def get_context_data(self, **kwargs) :
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context



# tag
def tag_page(request, slug) :
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
        {  
            'post_list' : post_list,
            'tag' : tag,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
        }
    )



# create post
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView) :  #UserPassesTestMixin : 권한이 주어진 사용자를 판별하는 클래스. 위에서 auth에 대해 import 후 사용
    model = Post
    form_class = PostForm
    # template_name = 'blog/post_form.html'이 내부에 생략되어 있으므로 따로 명시 안해도 됨
    # fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']  #forms.py 생성했으므로 필요없음

    # 이 페이지에 접근 가능한 사용자가 supersuer, staff인 경우에만 동작
    def test_func(self) :
        return self.request.user.is_superuser or self.request.user.is_staff 

    def form_valid(self, form) :
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser) :  #current_user.is_... : 로그인 사용자가 ...인 경우에 동작
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)

            # 태그를 ';'로 구분, 빈칸일 땐 넘김
            tags_str = self.request.POST.get('tags_str')
            if tags_str : 
                tags_str = tags_str.strip()

                tags_str = tags_str.replace(',', ';')
                tags_list = tags_str.split(';')
                print(tags_list)  #['unknown', ' 테스트', '']

                for t in tags_list :
                    t = t.strip()  #리스트의 문자열 공백 제거
                    print(t)

                    # t 공백일때 pass(for문 첫문장으로 이동, 다음 요소로 수행) 처리
                    if t == "" :
                        continue
                    
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)  #해당 태그가 존자하면 가져오고 없으면 새로 만듦
                    print(f'tag, is_tag_created : {tag}, {is_tag_created}')
                    
                    if is_tag_created :  #새로 만들어지면 slug 값 생성
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)  #tags 필드 추가

            return response
        else :
            return redirect('/blog/')
        


# update post 
# CBV
class PostUpdate(LoginRequiredMixin, UpdateView) :  # 이미 존재하는 포스트 사용자 로그인을 확인하기 위해 LoginRequiredMixin를 적고, PostCreate와 달리 UpdateView 추가
    model = Post
    form_class = PostForm  #summernote로 구현된 form.py 가져오기

    # 포스트 수정시 기존 태그가 자동으로 입력되는 코드 구현
    def get_context_data(self, **kwargs) :
        context = super(PostUpdate, self).get_context_data()
        if self.object.tags.exists() :
            tags_str_list = list()
            for t in self.object.tags.all() :
                tags_str_list.append(t.name)
            context['tags_str_default'] = '; '.join(tags_str_list)
        return context

    # 글을 작성한 사람만 글 수정 가능
    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated and request.user == self.get_object().author :  #로그인된 해당 포스트의 작성자에게만만 글 수정 버튼 노출
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else :
            raise PermissionDenied  #raise : 예외를 가져와 다시 발생시키는 것을 의미
        
    # tafs_str으로 받은 값을 태그로 쓰도록 코드 구현
    def form_valid(self, form) :
        response = super(PostUpdate, self).form_valid(form)
        self.object.tags.clear()

        # 태그를 ';'로 구분
        tags_str = self.request.POST.get('tags_str')
        if tags_str : 
            tags_str = tags_str.strip()
            tags_str = tags_str.replace(',', ';')
            tags_list = tags_str.split(';')

            for t in tags_list :
                    t = t.strip()  #리스트의 문자열 공백 제거
                    print(t)

                    # t 공백일때 pass(for문 첫문장으로 이동, 다음 요소로 수행) 처리
                    if t == "" :
                        continue

                    tag, is_tag_created = Tag.objects.get_or_create(name=t)  #해당 태그가 존자하면 가져오고 없으면 새로 만듦
                    print(f'tag, is_tag_created : {tag}, {is_tag_created}')
                    
                    if is_tag_created :  #새로 만들어지면 slug 값 생성
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)  #tags 필드 추가

            return response

        return response



# search post
class PostSearch(PostList) :
    # paginate_by = None

    def get_queryset(self) :
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(tags__name__contains=q) | Q(content__contains=q)
        ).distinct()
        return post_list
    
    def get_context_data(self, **kwargs) :
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'
        return context
    


# new comment
def new_comment(request, pk) :
    if request.user.is_authenticated :
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST' :
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid() :
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else :
            return redirect(post.get_absolute_url())
    else :
        raise PermissionDenied
    


# update comment
class CommentUpdate(LoginRequiredMixin, UpdateView) :
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated and request.user == self.get_object().author :
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else :
            raise PermissionDenied
        


# delete comment
def delete_comment(request, pk) :
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author :
        comment.delete()
        return redirect(post.get_absolute_url())
    else :
        raise PermissionDenied