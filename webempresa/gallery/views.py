from django.shortcuts import render, get_object_or_404
from blog.models import Post  # Asegúrate de importar el modelo Post desde la aplicación blog
from .models import imageDescription
# Create your views here.
def gallery(request):
    gallerys = imageDescription.objects.all()
    return render(request, "gallery/galeria.html",{'gallerys':gallerys})
    return render(request, "gallery/galeria.html")

def gallery_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    images = imageDescription.objects.filter(post=post)
    return render(request, 'gallery/galeria.html', {'post': post, 'images': images})