from django.shortcuts import render, redirect


# Create your views here.
from retake_exam.games_app.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, \
    EditProfileForm, DeleteProfileForm
from retake_exam.games_app.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if profile:
        no_profile = False
    else:
        no_profile=True
    context = {
        'profile': profile,
        'no_profile': no_profile,

    }
    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'create-profile.html', context)


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    if len(games) > 0:
        has_games = True
    else:
        has_games = False
    context = {
        'profile': profile,
        'games': games,
        'has_games': has_games,
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()
    context = {
        'form': form,
    }
    return render(request, 'create-game.html', context)


def details_game(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)
    context = {
        'profile': profile,
        'game': game,
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'delete-game.html', context)


def profile_details(request):
    profile = get_profile()
    games_count = len(Game.objects.all())
    full_name = ''
    if profile.first_name:
        full_name += profile.first_name
    if profile.last_name:
        full_name += ' ' + profile.last_name

    if games_count == 0:
        ratings_average = 0
    else:
        ratings_average = sum([game.rating for game in Game.objects.all()]) / games_count
    context = {
        'profile': profile,
        'games_count': games_count,
        'ratings_average': ratings_average,
        'full_name':full_name,
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)


