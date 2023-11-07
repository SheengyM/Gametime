from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category  # Import the Post model, Category model 
from .forms import PostForm 
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id' ] #the latest post ontop
    
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html',{'cats':cats.title(), 'category_posts':category_posts})

#class CategoryView(TemplateView):
 #   template_name = 'categories.html'
  #  category_posts = Post.objects.filter(category=cats)

    
    
class ArticleDetailView(DetailView):
    model = Post 
    template_name = 'article_details.html'
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
   # fields = ['title', 'title_tag', 'body']
   
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
   # fields = ['title', 'title_tag', 'body']
    success_url = reverse_lazy('home')