from django.db import transaction
from rest_framework import serializers

from orders.models import Order, Item
from products.models import Product


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['product', 'quantity', 'price', 'id']
        read_only_fields = ['id', 'price']


class ItemField(serializers.RelatedField):
    def to_representation(self, value):
        return ItemSerializer(value).data

    def to_internal_value(self, data):
        try:
            product = Product.objects.get(pk=data['product'])
            return {**data, "product": product}
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product does not exist")


class OrderSerializer(serializers.ModelSerializer):
    items = ItemField(queryset=Item.objects.all(), many=True, source='item_set')

    class Meta:
        model = Order
        fields = ['items', 'email', 'phone_number', 'country', 'city',
                  'zip_code', 'state', 'username']

    @transaction.atomic
    def create(self, validated_data):
        items = validated_data.pop('item_set')
        order = Order.objects.create(**validated_data)
        for item in items:
            Item.objects.create(order=order, price=item["product"].unit_price, **item)
        return order

    """
    {
    "items": [
{"product":1,"quantity":2}
],
    "email": "jsjdjsj@gmail.com",
    "phone_number": "012345678910",
    "country": "Egypt",
    "city": "Cairo",
    "zip_code": "12334",
    "state": "embaba",
    "username": "mostafa"
}
    """
