from rest_framework import serializers
from .models import Step, Ingredient, Recipe


class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('id','url', 'step_text','recipe')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id','url', 'text','recipe')

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id','url', 'name')
"""
class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username', 'first_name','last_name')"""