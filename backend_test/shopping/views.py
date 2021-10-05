from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import (
    IsAuthenticated
)

class ShoppingListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListModelSerializer

    def get_queryset(self):
        shopping_list = ShoppingList()
        # print(shopping_list.calculate_cost(self.queryset))
        return ShoppingList.objects.filter(user=self.request.user)

class ShoppingListItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemModelSerializer

