import re

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.


def validate_only_letters_and_underscores(value):
    if not re.match(r'^[A-Za-z_]+$', value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 2
    MIN_AGE = 0
    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            MinLengthValidator(MIN_LEN_USERNAME),
            validate_only_letters_and_underscores,
        )
    )

    email = models.EmailField(

    )
    age = models.PositiveIntegerField(
        null=True,
        blank = True,
    )

#OR USE MinValueValidator instead


class Album(models.Model):
    album_name = models.CharField(
        unique=True,
        max_length=30,
    )
    artist = models.CharField(
        max_length=30,
    )
    genre = models.CharField(
        max_length = 30,
        choices=(
            ("Pop Music", "Pop Music"),
            ("Jazz Music", "Jazz Music"),
            ("R & B Music", "R & B Music"),
            ("Rock Music", "Rock Music"),
            ("Country Music", "Country Music"),
            ("Dance Music", "Dance Music"),
            ("Hip Hop Music", "Hip Hop Music"),
            ("Other", "Other"),
        ))
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField()
    price = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ],

    )
    # user_profile = models.ForeignKey(
    #     Profile,
    #     on_delete=models.CASCADE,
    # )