from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titre' , 'content']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class' : 'input input-bordered input-sm mb-5',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class' : 'w-900 input input-bordered input-sm',
                'rows': 5,

            }),
        }