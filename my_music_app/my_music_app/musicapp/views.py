from django.shortcuts import render, redirect


# Create your views here.
from my_music_app.musicapp.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, \
    DeleteProfileForm
from my_music_app.musicapp.helpers import get_profile, get_albums
from my_music_app.musicapp.models import Profile, Album
from my_music_app.musicapp.templatetags.profiles import has_profile


def crud_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        profile_form = form_class(request.POST, instance=instance)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(success_url)

    context = {
        'profile_form': form_class(instance=instance),
    }
    return render(request, template_name, context)


def create_profile(request):

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    albums = get_albums()
    context = {
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateAlbumForm()
    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    context = {
        'profile': profile,
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums_count = len(Album.objects.all())
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
