from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from intro_to_django.tasks.models import Task_original


# def home(request):
#     items = Task_original.objects.all()
#     item_strings = (f'<li>{t.title}</li>' for t in items)
#     items_string = ''.join(item_strings)
#     html = f'''
# <h1>It works!</h1>
# <ul>
#    {items_string}
# </ul>
#      '''
#     return HttpResponse(html)

def home(request):
    context = {
        'title': 'It works from View!',
        'tasks': Task_original.objects.all(),

    }
    return render(request, 'home.html', context)