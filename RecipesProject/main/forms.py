
from django import forms

from RecipesProject.main.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time',)