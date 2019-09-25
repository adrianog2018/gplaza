from django.shortcuts import render
from rest_framework import viewsets
from . models import Step, Ingredient, Recipe, Usermodel
from . serializers import StepSerializer, IngredientSerializer, RecipeSerializer, UsermodelSerializer
#from .forms import ExtendedUserCreationForm, UserProfileForm

# Create your views here.

class StepView(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer



class UsermodelView(viewsets.ModelViewSet):
    queryset = Usermodel.objects.all()
    serializer_class = UsermodelSerializer
    
