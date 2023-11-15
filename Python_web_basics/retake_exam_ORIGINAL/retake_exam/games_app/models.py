from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.



class Profile(models.Model):
    MIN_AGE = 12

    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_PASSWORD = 30
    email = models.EmailField(

    )
    age = models.IntegerField(
        validators=(
            MinValueValidator(MIN_AGE),
    ))
    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
    )
    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=True,
        blank=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=True,
        blank=True,
        verbose_name='Last Name',

    )

    image = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

class Game(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_CATEGORY = 15
    title = models.CharField(
        max_length= MAX_LEN_TITLE,
    )
    category = models.CharField(
        max_length=MAX_LEN_CATEGORY,
        choices=(
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Puzzle", "Puzzle"),
            ("Strategy", "Strategy"),
            ("Sports", "Sports"),
            ("Board/Card Game", 'Board/Card Game'),
            ("Other", "Other"),
    ),
    )
    rating = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(5.0)],
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(1),
        ),
        verbose_name='Max Level',
    )
    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name="Image URL",
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )







