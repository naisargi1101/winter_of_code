from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from .models import Post,Comment
from django.forms import ModelForm, Select,TextInput

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','companyName','typeOfOffer','jobProfile','content','status','author']
        labels = {
            'title': 'Post Title',
            'slug': 'Slug',
            'companyName': 'Company Name',
            'typeOfOffer': 'Type of Offer',
            'jobProfile': 'Job Profile',
            'content': 'Post Content',
            'status': 'Post Status',
            'author':''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the post title'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'companyName': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the company name'}),
            'typeOfOffer': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the type of offer'}),
            'jobProfile': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the job profile'}),
            'content': SummernoteWidget(),
            'status': forms.Select(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'style':'display:none;'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
