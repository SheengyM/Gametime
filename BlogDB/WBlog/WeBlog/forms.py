from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blog Title!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag!'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'Bauthor'}),
            'category': forms.Select(attrs={'class': 'form-control'}),  # Update widget to a select field
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog Description!'}),
        }




class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blog Title!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag!'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog Description!'}),
        }
        
        
        
