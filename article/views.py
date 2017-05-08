# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Article
from datetime import datetime
from django.http import Http404
import random
import os
# Create your views here.
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})


def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def sj(request):
	return HttpResponse("打印一个随机数：%s" %random.randint(1,100))

def index(request):
	return render(request, 'index.html', {'current_time': datetime.now()})

def home(request):
	post_list = Article.objects.all()
	return render(request, 'home.html', {'post_list' : post_list})

def about_me(request):
    post_list = Article.objects.all()
    return render(request, 'aboutme.html', {'post_list' : post_list})


def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 
                                            'error' : False})

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})
