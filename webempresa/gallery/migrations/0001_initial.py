# Generated by Django 4.2.9 on 2024-01-23 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0003_alter_post_categories'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='imageDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='blog.post', verbose_name='Entrada del Blog')),
            ],
            options={
                'verbose_name': 'galeria',
                'verbose_name_plural': 'galerias',
                'ordering': ['-created'],
            },
        ),
    ]
