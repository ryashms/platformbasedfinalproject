from django.urls import path
from post.views import (
    create_blog_view)

app_name= 'post'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
]

