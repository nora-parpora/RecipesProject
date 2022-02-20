from django.shortcuts import render, redirect

from RecipesProject.main.forms import CreateRecipeForm
from RecipesProject.main.models import Recipe


def home(requests):
    recipes = Recipe.objects.all()
    available_recipes = False
    if len(recipes) > 0:
        available_recipes = True

    context = {
        'recipes': recipes,
        'available_recipes':available_recipes,
    }
    return render(requests, 'index.html', context)


def create(request):
    instance = Recipe()
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateRecipeForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def edit(requests, pk):
    pass


def delete(requests, pk):
    pass


def details(requests, pk):
    pass

