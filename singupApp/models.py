from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_code = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.project_name


class Personal(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField(blank_label='Select Country')
    money = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')


class AdditionInfo(models.Model):
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


class UserAdditionInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_query_name='userinfo')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    department = models.ForeignKey(AdditionInfo, on_delete=models.CASCADE)
