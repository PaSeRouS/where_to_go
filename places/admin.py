from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    fields = ('image', 'get_preview', 'image_id')

    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        prop_height = 200
        prop_width = prop_height * obj.image.width / obj.image.height

        return format_html('<img src="{}" width="{}" height={} />',
            obj.image.url,
            prop_width,
            prop_height,
        )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
