
from django import forms

from RecipesProject.main.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time',)


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time',)


class DeleteRecipeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.fields.values():
            v.disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time',)