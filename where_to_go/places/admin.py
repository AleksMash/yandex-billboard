from django.contrib import admin
from django.utils.html import format_html


from .models import Place, Image

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    verbose_name_plural = 'Фотографии'
    fields = ['image', 'preview_image', 'position']
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        width = obj.image.width * 200/obj.image.height
        return format_html('<img src="{}" width="{}px" height="200px" />',
                           obj.image.url, width)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

admin.site.register(Image)

