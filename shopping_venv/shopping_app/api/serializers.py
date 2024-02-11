from rest_framework import serializers
from .models import ShoppingItems

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItems
        fields = 'id','item_name','item_desc','item_img','item_price'
