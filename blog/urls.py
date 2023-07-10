from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog_home'),
    path('blog/<int:id>', views.blog_detail, name='blog_detail'),
    path('blog/blog_page', views.blog, name='blog'),
    path('blog/author', views.author, name='author'),
]
