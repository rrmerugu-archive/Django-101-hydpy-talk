# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from blog.models import BlogPost
from django.shortcuts import get_object_or_404
# Create your views here.


def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog-list.html', {'blogs': blogs})


def blog_view(request, post_id):
    blog = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog-view.html', {'blog': blog})
