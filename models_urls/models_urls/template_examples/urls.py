from django.urls import path

from models_urls.template_examples.views import index

urlpatterns = [
    path('', index, name = 'templates index')
]