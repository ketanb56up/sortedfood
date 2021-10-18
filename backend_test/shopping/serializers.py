# Add your serializers here
from rest_framework import serializers
from .models import *

class ShoppingListModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = ShoppingList
        fields = '__all__'

class ShoppingListItemModelSerializer(serializers.ModelSerializer):
    # ingredient = serializers.CharField(source='ingredient.name')
    # shopping_list = serializers.CharField(source='shopping_list.title')

    class Meta:
        model = ShoppingListItem
        fields = '__all__'
