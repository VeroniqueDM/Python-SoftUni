from django.contrib import admin

# Register your models here.
from exam_prep.web.models import Profile, Expense


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name',
    )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title',
    )
