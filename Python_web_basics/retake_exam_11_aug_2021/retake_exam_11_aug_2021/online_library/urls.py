import profile

from django.urls import path

from retake_exam_11_aug_2021.online_library.views import show_index, add_book, edit_book, book_details, profile_details, \
    profile_edit, profile_delete, create_profile, book_delete

urlpatterns = [
    path('', show_index, name='home page'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('delete/<int:pk>', book_delete, name='delete book'),
    path('details/<int:pk>', book_details, name='details book'),
    path('profile/', profile_details, name='details profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', profile_edit, name='edit profile'),
    path('profile/delete/', profile_delete, name='delete profile'),

]
