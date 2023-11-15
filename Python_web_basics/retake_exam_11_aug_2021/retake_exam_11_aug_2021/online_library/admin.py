from django.contrib import admin

# Register your models here.
from retake_exam_11_aug_2021.online_library.models import Profile, Book


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name',
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'type',
    )

