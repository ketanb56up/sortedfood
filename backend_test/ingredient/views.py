from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import (
    IsAuthenticated
)

# Views for all the Ingredient API's
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientModelSerializer

