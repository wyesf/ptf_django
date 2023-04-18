from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag, Comment


# summernote 관련 라이브러리
from django_summernote.admin import SummernoteModelAdmin
# from .models import SomeModel


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin) :
    prepopulated_fields = {'slug' : ('name', )}

class TagAdmin(admin.ModelAdmin) :
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)