"""snapchat URL Configuration

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
from django.urls import path
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about.html/',about,name='about'),
    path('contact.html/',contact,name='contact'),
    path('service.html/',service,name='service'),
    path('product.html/',product,name='product'),
    path('team.html/',team,name='team'),
    path('testimonial.html/',testimonial,name='testimonial'),
    path('feature.html/',feature,name='feature'),
    path('blog.html/',blog,name='blog'),
    path('detail.html/',blog,name='detail'),
    path('farmstore/',register,name='register'),
    path('farmlist/',farm_list,name='farm_list'),
    path('registercust/',register_cust,name='register_cust'),
    path('userlogin/',user_login,name='user_login'),
    path('userlogout/',user_logout,name='user_logout'),

    






]
