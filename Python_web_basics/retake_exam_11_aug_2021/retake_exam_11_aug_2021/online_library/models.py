from django.db import models

# Create your models here.


class Profile(models.Model):
    MAX_LENGTH_FIRST_NAME = 30
    MAX_LENGTH_LAST_NAME = 30
    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
    )
    image_url = models.URLField(

    )


class Book(models.Model):
    MAX_LENGTH_TITLE = 30
    MAX_LENGTH_TYPE = 30
    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
    )
    description = models.TextField(

    )
    image = models.URLField(

    )
    type = models.CharField(
        max_length=MAX_LENGTH_TYPE,
    )

