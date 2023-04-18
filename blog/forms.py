from django import forms
from .models import Post
from .models import Comment

from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px', 'font-family': 'arial'}}),
        }

# comment field 추가
class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ('content',)
        # exclude = ('post', 'author', 'created_at', 'modified_at',)