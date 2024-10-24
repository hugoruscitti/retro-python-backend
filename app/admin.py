from django.contrib import admin
from app.models import Proyecto
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto
    list_display = (
            'id', 
            'screenshot_tag',
            'textura_tag',
            'hash',
            'url', 
    )
    search_fields = (
            'hash', 
            'id',
    )

    def url(self, obj):
        hash = str(obj.hash)
        return format_html(f"<a target='_blank' href='http://app.pilas-engine.com.ar/#/proyecto/{hash}'>ver</a>")

    def screenshot_tag(self, obj):
        return mark_safe(f"<img src=\"{obj.screenshot}\" width=\"160\">")

    def textura_tag(self, obj):
        return mark_safe(f"<img src=\"{obj.textura}\" width=\"160\">")

admin.site.register(Proyecto, ProyectoAdmin)
