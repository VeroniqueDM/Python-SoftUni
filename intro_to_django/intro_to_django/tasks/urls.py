from django.urls import path

from intro_to_django.tasks.views import home

urlpatterns = [

    path('', home),
]
