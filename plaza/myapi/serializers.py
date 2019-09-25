from rest_framework import serializers
from . models import Step, Ingredient, Recipe, Usermodel

class UsermodelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usermodel
        fields = ('id','url','user','first_name','last_name','email')
      
     
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

