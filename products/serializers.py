from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
         model = Product
         fields = '__all__'

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError(
                'Цена не может быть отрицательной'
            )
        return price