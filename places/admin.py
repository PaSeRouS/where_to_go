from django.contrib import admin

from .models import Image, Place

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
