
# Register your models here.
from django.contrib import admin

from .models import Step, Ingredient, Recipe


admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(Recipe)
#admin.site.register(UserProfile)