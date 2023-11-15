from django.contrib import admin

# Register your models here.
from my_music_app.musicapp.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username',
    )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'album_name', 'artist',
    )
    
