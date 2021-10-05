from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import (
    IsAuthenticated
)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientModelSerializer

