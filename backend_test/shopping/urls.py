from .views import *
from django.urls import path, include
# from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('list', ShoppingListViewSet, basename='shoppinglist')
router.register('listitem', ShoppingListItemViewSet, basename='shoppinglistitem')


urlpatterns = [
    path("", include(router.urls)),

]
