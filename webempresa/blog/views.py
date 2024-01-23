from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from gallery.models import imageDescription
# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html",{'posts':posts})
    return render(request, "blog/blog.html")

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html",{'category':category})
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'galeria.html', {'post': post})