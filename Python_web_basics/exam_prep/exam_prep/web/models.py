from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    if not all(c.isalpha() for c in value):
        raise ValidationError("Ensure this value contains only letters.")


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        mb_limit = self.max_size
        if filesize > mb_limit * 1024 * 1024:
            raise ValidationError("Max file size is 5.00 MB")


class Profile(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_FIRST_NAME = 15
    MAX_LEN_LAST_NAME = 15
    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,

        )
    )
    budget = models.FloatField(
        default=0,
        validators=(
            MinValueValidator(0),
        ),
    )
    image = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(5),
        ),
    )


class Expense(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    image = models.URLField(
        verbose_name='Link to Image:',
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField(

    )

    class Meta:
        ordering = ('title', 'price',)
