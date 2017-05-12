# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from blog.models import BlogPost
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog-list.html', {'blogs': blogs})


def blog_list_paginated(request):
    """
    https://docs.djangoproject.com/en/1.11/topics/pagination/
    
    :param request:
    :return:
    """
    blogs_list = BlogPost.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(blogs_list, 5)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'blog-list-paginated.html', {'blogs': blogs})

def blog_view(request, post_id):
    blog = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog-view.html', {'blog': blog})