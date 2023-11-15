from django.contrib import admin
from intro_to_django.tasks.models import Task_original

# Register your models here.

# # Variant 1
# admin.site.register(Task_original)

# Variant 2
@admin.register(Task_original)
class Task_originalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)