# Generated by Django 4.0.2 on 2022-02-20 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_model_recipemodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeModel',
            new_name='Recipe',
        ),
    ]
