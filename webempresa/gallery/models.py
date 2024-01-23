from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from blog.models import Post
# Create your models here.
class imageDescription(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripcion")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="gallery", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    post = models.ForeignKey(Post, verbose_name="Entrada del Blog", related_name="gallery_images",
                             on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = "galeria"
        verbose_name_plural = "galerias"
        ordering = ["-created"]

    def __str__(self):
        return self.title


