# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import BlogPost
# Create your views here.


def index_page(request):
    return render(request, 'homepage.html', {})


def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog-list.html',
                  {'blogs': blogs})


def blog_view(request, post_id):
    blog = BlogPost.objects.get(id=post_id)
    return render(request, 'blog-view.html',
                  {'blog': blog})