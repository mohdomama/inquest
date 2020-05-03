from django.urls import path

from .views import (
    blog_post_detail_page,
    blog_post_list_page,
    blog_post_delete_page,
    blog_post_update_page,
    blog_post_create_page
)

urlpatterns = [
    path('post/<str:slug>/', blog_post_detail_page),
    path('post/<str:slug>/delete', blog_post_delete_page),
    path('post/<str:slug>/update', blog_post_update_page),
    path('', blog_post_list_page, name='news'),
    path('create/', blog_post_create_page)
]
