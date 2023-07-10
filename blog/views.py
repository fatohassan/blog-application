from django.shortcuts import render
from blog.models import BlogPost, Author
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

# Create your views here.

def blog_list(request):
    blogs = BlogPost.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog/index.html', context)

def blog_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('blog_home'))
            blog = BlogPost.objects.get(id=id)
        context = {'blog':blog}
        return render(request, 'blog/blog_detail.html', context)
    except:
        HttpResponse

def blog(request):
    blog_page = BlogPost.objects.all()
    context = {'blog_page':blog_page}
    return render(request, 'blog/blog.html', context)

def author(request):
    author = Author.objects.all()
    context = {'author': author}
    return render(request, 'blog/author.html', context)



