from django.contrib import admin
from .models import imageDescription

# Register your models here.

class ImageDescriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'published'


admin.site.register(imageDescription, ImageDescriptionAdmin)
