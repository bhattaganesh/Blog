from django.forms.widgets import Select, TextInput, Textarea
from .models import Post, Category
from django import forms

class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=TextInput(attrs={'class' : 'form-control'}))
    content = forms.CharField(widget=Textarea(attrs={'class' : 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=Select(attrs={'class' : 'form-control'}))
    class Meta:
        model = Post
        # fields = '__all__'
        # fields = ['title','image','content','category']
        exclude = ['status']