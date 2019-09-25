from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('steps', views.StepView)
router.register('ingredients', views.IngredientView)
router.register('recipes', views.RecipeView)
router.register('users', views.UsermodelView)

urlpatterns = [
    path('', include(router.urls))

]
