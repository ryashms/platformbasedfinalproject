from django.shortcuts import render
from post.models import ImagePost

def home_screen_view(request):
    context = {}
    blog_posts = ImagePost.objects.all()
    context['blog_posts'] = blog_posts
    return render(request, "personal/home.html", context)

