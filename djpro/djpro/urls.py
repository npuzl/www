"""HelloWorld URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from learn import views as learn_views  # new
from django.conf.urls import url

urlpatterns = [

    # path('blog/', learn_views.blog, name='blog'),
    path("", learn_views.home, name='index'),  # new
    path('admin/', admin.site.urls),
    url(r'Page/(.*)', learn_views.toPage, name='toPage'),
    path('blog/',learn_views.blogPage, name='myBlog'),
    #path('blog/', include('learn.urls', namespace='learn'))
]
