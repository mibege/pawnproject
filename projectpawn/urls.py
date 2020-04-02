"""projectpawn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from accounts.views import home, LogInView, SignUpView, LogOutView, ChangePasswordView
from userprofile.views import indexUserProfile, indexMapProfile
from django.conf.urls import url
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='index'),
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('log-out/', LogOutView.as_view(), name='log_out'),
    path('update/profile/', indexUserProfile.as_view(), name='post_user_view'),
    path('change/password/', ChangePasswordView.as_view(), name='change_password'),
    path('dogwalker/area', indexMapProfile, name='post_user_map'),
    url(r'^booking/', include('booking.urls'), name='post_booking'),
]
