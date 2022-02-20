from django.contrib import admin
from django.urls import path

from RecipesProject.main.views import home, create, edit, details, delete

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('details/<int:pk>/', details, name='details'),
    path('delete/<int:pk>/', delete, name='delete'),

]
