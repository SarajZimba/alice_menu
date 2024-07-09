from order.models import Order, OrderDetails
from rest_framework import serializers
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = [
            "created_at",
            "updated_at",
            "status",
            "is_deleted",
            "sorting_order",
            "is_featured"
        ]
    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
class OrderDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetails
        exclude = [
            "created_at",
            "updated_at",
            "status",
            "is_deleted",
            "sorting_order",
            "is_featured"
        ]

    def create(self, validated_data):
        return OrderDetails.objects.create(**validated_data)