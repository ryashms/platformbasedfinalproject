from django.shortcuts import render, redirect
from post.forms import CreateBlogPostForm
from post.models import ImagePost
def create_blog_view(request):
    context = {}
    
    if request.method == 'POST':
        form = CreateBlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user

            obj = form.save(commit=False)
            obj.author = author
            obj.save()

            form = CreateBlogPostForm()
    else:
        form = CreateBlogPostForm()

    context['form'] = form

    blog_posts = ImagePost.objects
    context['blog_posts'] = blog_posts

    return render(request, "create_image.html", context)







