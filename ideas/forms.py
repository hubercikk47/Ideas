from django import forms
from django.contrib.auth.models import User
from .models import Idea, Comments


class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['name', 'description', 'status', 'date', 'author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['author', 'content', 'date', 'idea']