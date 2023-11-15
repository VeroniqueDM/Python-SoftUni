from django.contrib import admin

# Register your models here.
from retake_exam.games_app.models import Profile, Game


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'email',
    )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category',
    )
