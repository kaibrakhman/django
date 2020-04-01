from django import forms
from .models import Post

class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']
