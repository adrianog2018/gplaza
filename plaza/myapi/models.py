from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usermodel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(unique=True, max_length=254, default='')
    #password = models.ForeignKey(User.password, on_delete=models.CASCADE)
    # add additional fields in here
    
    def __str__(self):
        return self.first_name


class Recipe(models.Model):
    name = models.CharField(max_length=50, null=False, default='')
    #user = models.ForeignKey(Usermodel, on_delete=models.CASCADE)

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
