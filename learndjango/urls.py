"""learndjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from pages.views import homepage_view, contact, what_we_do ,about
from foundation.views import foundation_detail_view, foundation_create_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage_view,name='home'),
    path('contact_us/',contact,name='contact'),
    path('about_us/',about,name='about'),
    path('what_we_do/', what_we_do, name='what we do'),
    path('create/', foundation_create_view),
    path('foundation/', foundation_detail_view)

    ]
