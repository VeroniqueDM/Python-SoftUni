from django.db import models

# Create your models here.

# class Task(models.Model):
#     title = models.CharField(
#         max_length=20,
#
#     )
#     text = models.CharField(
#         max_length=40,
#     )
class Task_original(models.Model):
    title = models.CharField(
        max_length=20,

    )
    text = models.CharField(
        max_length=40,
    )

    def __str__(self):
        return f'{self.id}: {self.title}'