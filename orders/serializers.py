from rest_framework import serializers
from .models import Cart, CartItem, Order

class CartItemSerializer(serializers.Serializer):
    
    product_name = serializers.CharField(source='product.name', read_only=True)
    price = serializers.CharField(source='product.price', read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'product_name', 'quantity', 'price']

class CartSerializer(serializers.ModelSerializer):
    # Nested serializer to include all cart items
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at']
    
    
    def get_total_price(self, obj):
        return sum([item.product.price * item.quantity for item in obj.items.all()])
 
    
    
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'created_at']