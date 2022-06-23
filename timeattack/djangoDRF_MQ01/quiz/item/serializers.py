from rest_framework import serializers

from .models import Category as CategoryModel, Item
from .models import Item as ItemModel

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = "__all__"