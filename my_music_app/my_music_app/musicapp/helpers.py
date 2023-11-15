import re

from django.core.exceptions import ValidationError

from my_music_app.musicapp.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def get_albums():
    albums = Album.objects.all()
    if albums:
        return albums
    return None


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value Must be positive')


# def validate_only_letters(value):
#     if not all(c.isalpha() for c in value):
#         raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


# class BootstrapMixin:
#     fields = {}
#     def _init_bootstrap_form_controls(self):
#         for _, field in self.fields.items():
#             if not hasattr(field.widget, 'attrs'):
#                 setattr(field.widget, 'attrs', {})
#             if 'class' not in field.widget.attrs:
#                 field.widget.attrs['class'] = ''
#             field.widget.attrs['class'] += 'form-control'
