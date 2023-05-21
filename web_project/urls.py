"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ex2 import views

urlpatterns = [
    path('admin/', admin.site.urls, ),
    path('', views.home_views, name = "home"),
    path('start/', views.home_views),
    path('contact/', views.contact_views, name="contact"),
    path('about/', views.about_view, name="about"),
    path('about-me/', views.about_view),
    #path('news/', views.news_view),
    path('covid19/', include('covid19.urls')),
    path('blog/', include('blog.urls')),
    path('biotools/', include('biotools.urls')),
]

urlpatterns += staticfiles_urlpatterns()