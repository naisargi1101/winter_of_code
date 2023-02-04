from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from .models import Post
from django.forms import ModelForm, Select,TextInput

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','content','status']
        widgets = {
            'content':SummernoteWidget(),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
        }
