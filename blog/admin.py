from django.contrib import admin
from blog.models import *


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title']
    search_fields = []
    list_select_related = True
    
    fieldsets = [
        (None, {'fields': ['title', 'title_slug', 'sub_title', 'teaser_html', 'text_html', 'media','tags']})
    ]
    
class MediaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Media._meta.fields]
    search_fields = []
    list_select_related = True
    
    fieldsets = [
        (None, {'fields': ['name', 'media_file', 'subtitle']})
    ]
    
class TagAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tag._meta.fields]
    search_fields = []
    list_select_related = True
    
    fieldsets = [
        (None, {'fields': ['name']})
    ]

admin.site.register(Entry, EntryAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Tag, TagAdmin)
