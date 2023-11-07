from django import forms
from .models import Post, Category

#choices = [('Coding, coding'),('tutoring, Tutoring'), ('hacking, Hacking'),   ('Education', 'education')]

choices = Category.objects.all().values_list('name', 'name')

choices_list = []

for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blog Title!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag!'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': ' Blog Author!'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' Blog Description!'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blog Title!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag!'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' Blog Description!'}),

    }