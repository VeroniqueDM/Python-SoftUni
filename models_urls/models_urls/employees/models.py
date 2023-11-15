from django.db import models
from django.core import validators

# Create your models here.
from django.urls import reverse


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        null=True,
    )
    class Meta:
        abstract=True
class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
        null=True,
    )
    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse('department details', kwargs={
    #         'id': self.id
    #     })

class Employees(models.Model):
    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    COMPANIES = (SOFT_UNI, GOOGLE, FACEBOOK)
    first_name = models.CharField(
        #        default='Firstname',
        max_length=30,
        null=True

    )
    last_name = models.CharField(
        #       default='Lastname',
        max_length=40,
        null=True,
        blank=True,
    )
    egn = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        verbose_name='EGN',
        validators=(
            validators.MinLengthValidator(10),
        ),

    )
    job_title = models.IntegerField(
 #       max_length=20,
        choices=(
            (1,'Software Engineer'),
            (2, 'Dev Ops'),
            (3, 'QA')
        ),
        null=True
    )
    # company = models.CharField(
    #     max_length=max(len(c) for c in COMPANIES),
    #     choices= ((c, c) for c in COMPANIES),
    #     null=True
    # )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to= 'profiles'

    )
    class Meta:
        ordering = ('first_name', '-last_name') #initial ordering is by first name, can use more than one arg and desc ord is done with a -

class Project(models.Model):
    name = models.CharField(
        max_length=30,
        null=True,
    )
    dead_line = models.DateField(
        null=True,
        blank=True,
    )
    employees = models.ManyToManyField(
        to=Employees,
        null=True,
    )

class User(models.Model):
    email = models.EmailField()
    employee = models.OneToOneField(
        Employees,
        on_delete=models.CASCADE,
        primary_key=True,
    )