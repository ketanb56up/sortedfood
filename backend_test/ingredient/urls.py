from .views import *
from django.urls import path, include
# from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router for Ingredient API's
router.register('', IngredientViewSet, basename='ingredient')


urlpatterns = [
    path("", include(router.urls)),

]
