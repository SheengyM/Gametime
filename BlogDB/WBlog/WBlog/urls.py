"""
URL configuration for WBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from members.views import UserRegisterView  # Import your custom view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WeBlog.urls')),
    path('members/register/login/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('members/register/', UserRegisterView.as_view(), name='register'),  # Define your custom URL pattern
]


