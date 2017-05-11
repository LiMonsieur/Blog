# -*- coding: UTF-8 -*-
"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home , name = 'home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name = 'archives'),
    url(r'^aboutme/$', views.about_me, name = 'about_me'),
    url(r'^tag(?P<tag>\w+)/$',views.search_tag, name = 'search_tag'),
    url(r'^search/$',views.blog_search, name = 'search'),
    url(r'^sj', views.sj),
    url(r'^index/$', views.index),

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
