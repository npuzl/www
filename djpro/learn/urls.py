from django.urls import path
from . import views

app_name = 'learn'
urlpatterns = [
    path('blogPage/', views.blogPage, name='myBlog')
]
