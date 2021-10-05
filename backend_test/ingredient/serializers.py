# Add your serializers here
from rest_framework import serializers
from .models import *

class IngredientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'

