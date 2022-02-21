from django.shortcuts import render, redirect

from RecipesProject.main.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
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


def edit(request, pk):
    instance = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditRecipeForm(instance=instance)

    context = {
        'form': form,
        'instance': instance,
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    instance = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = DeleteRecipeForm(instance=instance)
    context = {
        'form': form,
        'instance': instance,
    }
    return render(request, 'delete.html', context)


def details(request, pk):
    instance = Recipe.objects.get(pk=pk)
    list_of_ingredients = instance.ingredients.split(", ")

    context = {
        'instance': instance,
        'list_of_ingredients': list_of_ingredients,
    }
    return render(request, 'details.html', context, )

