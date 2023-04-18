from django.urls import path
from . import views

urlpatterns = [
    # delete_comment/<int:pk>/
    path('delete_comment/<int:pk>/', views.delete_comment),
    # update_comment/<int:pk>/
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view(), name='update_comment'),
    # /blog/update_post/포스트의pk/로 접근할 때 postUpdate 사용
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name='post_updete'),
    # search/<str:q>/
    path('search/<str:q>/', views.PostSearch.as_view(), name='post_search'),
    # path(create_post/,)
    path('create_post/', views.PostCreate.as_view(), name='post_create'),
    # tag/<str:slug>/
    path('tag/<str:slug>/', views.tag_page, name='tag_filter'),
    # /blog/category/{self.slug}/
    path('category/<str:slug>/', views.category_page, name='category_filter'),
    # <int:pk>/new_comment/
    path('<int:pk>/new_comment/', views.new_comment, name='new_comment'),
    # path('', views.index),
    path('', views.PostList.as_view(), name='post_list'),
    # path('<int:pk>/', views.detail_page, name='detail_page'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail_page'),
]