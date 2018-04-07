# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
from django.http import Http404

def home(req):
    post_list = Article.objects.all()
    return render(req, 'blog/home.html', {'post_list':post_list})

def Test(req):
    return render(req, 'blog/test.html', {'current_time': datetime.now()})

def Detail(req, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(req, 'blog/post.html', {'post':post})