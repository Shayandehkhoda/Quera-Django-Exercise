from django.contrib import admin
from .models import Musician, Album

class AlbumInLine(admin.StackedInline):
    model = Album
    extra = 0
@admin.register(Musician)
class music(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ['instrument']
    inlines = [AlbumInLine]
    
@admin.register(Album)
class alb(admin.ModelAdmin):
    list_display = ['id', 'name', 'artist', 'num_stars']
    sortable_by = ['name', 'artist']
    list_display_links = ['name', 'artist']




