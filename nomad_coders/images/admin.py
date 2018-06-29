from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display_links =(
        'location',
        'caption',
    )

    list_display= (
        'file',
        'location',
        'caption',
        'creator',
        'create_at',
        'update_at',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    
    list_display = (
        'creator',
        'image'
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'message',
        'creator',
        'image',
        'create_at',
        'update_at',

    )