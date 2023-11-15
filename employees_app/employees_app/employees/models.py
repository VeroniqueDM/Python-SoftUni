from random import choices

import blank
from django.core import validators

from django.db import models
from django.urls import reverse


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    class Meta:
        abstract = True

class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )
    def get_absolute_url(self):
        return reverse('department details', kwargs={
            'id': self.id,
        })
    def __str__(self):
        return f'Department {self.name}'

class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEVOPS_SPECIALIST = 3

    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    COMPANIES = (
        SOFT_UNI,
        GOOGLE,
        FACEBOOK,
    )
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )
    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name = 'EGN',
        validators = (
            validators.MinLengthValidator(10),
        )
    )

    job_title_t = models.IntegerField(

        choices=(
            (SOFTWARE_DEVELOPER, 'Python Dev'),
            (QA_ENGINEER,'QA Engineer'),
            (DEVOPS_SPECIALIST, 'DevOps Specialist'),
        ),
        verbose_name = 'Job Title'
    )

    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES),
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,

    )
    image = models.ImageField(
        null=True,
        blank=True,
        # upload_to='profiles'
    )

    class Meta:
        ordering = ('first_name', '-last_name')

class User(models.Model):
    username = models.EmailField()
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True
    )

class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    deadline = models.DateField(
        null=True,
        blank=True,
    )
    employees = models.ManyToManyField(
        to=Employee
    )