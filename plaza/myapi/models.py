from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""
class UserProfile(models.Model):
    username = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    #email = models.EmailField("email", max_length=254, unique=True)
    #first_name = models.CharField(max_lenght=50)
    #last_name = models.CharField(max_lenght=50)

    # add additional fields in here

    def __str__(self):
        return self.username
"""


class Recipe(models.Model):
    name = models.CharField(max_length=50, null=False, default='')

    def __str__(self):
        return self.name


class Step(models.Model):
    step_text = models.CharField(max_length=200, null=False, default='')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.step_text


class Ingredient(models.Model):
    text = models.CharField(null=False, max_length=50, default='')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
