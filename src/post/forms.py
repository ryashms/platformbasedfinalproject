from django import forms

from post.models import ImagePost 


class CreateBlogPostForm(forms.ModelForm):

	class Meta:
		model = ImagePost
		fields = ['title',  'image']

