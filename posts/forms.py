from django import forms
from .models import Post 
from django.db import models
from django.forms import fields

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'