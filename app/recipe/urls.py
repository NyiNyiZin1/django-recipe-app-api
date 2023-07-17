"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views

# Default url path(/api/recipe/)
# Default CRUD include
router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

# not url
app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
