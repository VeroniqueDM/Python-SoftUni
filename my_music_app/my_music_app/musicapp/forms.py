from django import forms

# from my_music_app.musicapp.helpers import BootstrapMixin
from my_music_app.musicapp.models import Profile, Album


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'username', 'email', 'age',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder':"Enter username",
                },


            ),
            'email':forms.TextInput(
                attrs={
                    'placeholder':"Enter email",
                },

            ),
                'age':forms.NumberInput(
                # attrs={
                #     'placeholder':"Enter URL"
                # },

            ),
        }

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'description': 'Description',
            'image': 'Image URL',
            'price': 'Price',
        }

class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'description': 'Description',
            'image': 'Image URL',
            'price': 'Price',
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'description': 'Description',
            'image': 'Image URL',
            'price': 'Price',
            'genre': 'Genre',
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):

        self.instance.delete()
        Album.objects.all().delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()
