"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
<<<<<<< HEAD
from django.shortcuts import render
from django.urls import path,include
=======
from django.urls import path
from django.conf.urls import include
>>>>>>> 49862b93723c67630896064f83c76df45f112b72

def home(request):
    return render(request,'home.html')
urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('accounts/',include('allauth.urls')),
    path("core/",include("core.urls")),
=======
    path('accounts/', include('allauth.urls')),
>>>>>>> 49862b93723c67630896064f83c76df45f112b72
]

