from rest_framework import serializers
from .models import Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()  # Display category name instead of ID

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'description']

    

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True, read_only=True) 

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'subcategories']
