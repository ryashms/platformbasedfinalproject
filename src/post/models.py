from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    file_path = 'images/{author_id}/{filename}'.format(
    author_id=str(instance.author.id),title=str(instance.title), filename=filename)

    
    return file_path

class ImagePost(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_location)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
