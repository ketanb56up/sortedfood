from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import (
    IsAuthenticated
)

class ShoppingListViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListModelSerializer

    # This is for filtering the shopping list based on the user and counting the total cost from the shopping list item.
    def get_queryset(self):
        shopping_list = ShoppingList()
        response=[]
        listdict=dict()
        shoppinglist = ShoppingList.objects.filter(user=self.request.user)
        for eachlist in shoppinglist:
            res = shopping_list.calculate_cost(eachlist)
            listdict['id'] = eachlist.id
            listdict['user'] = eachlist.user
            listdict['title'] = eachlist.title
            listdict['total_cost'] = res
            response.append(listdict)
        return response

class ShoppingListItemViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemModelSerializer

