from django.contrib import admin
from .models import Project
from django.utils.html import format_html

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'github_link', 'image_tag')
    list_filter = ('technology',)
    search_fields = ('title', 'technology', 'description')
    ordering = ('title',)

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<a href="{0}" target="_blank">'
                '<img src="{0}" width="80" height="50" style="object-fit: cover; border-radius: 4px;"/>'
                '</a>',
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Image'