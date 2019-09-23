from django.shortcuts import render
from rest_framework import viewsets
from .models import Step, Ingredient, Recipe
from .serializers import StepSerializer, IngredientSerializer, RecipeSerializer
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
"""
class CustomUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer"""