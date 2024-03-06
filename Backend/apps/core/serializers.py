from rest_framework import serializers
from apps.products.models import Product
from apps.categories.models import Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'slug', 'featured', 'price', 'thumbnail', 'description', 'in_stock', 'created_date', 'updated']
