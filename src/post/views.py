from django.shortcuts import render, redirect
from .forms import PostForm

def create_image_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = PostForm()
    
    return render(request, 'create_image.html', {'form': form})
