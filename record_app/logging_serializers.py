from rest_framework import serializers
from .models import Product, Category


class CategoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductLogSerializer(serializers.ModelSerializer):
    categorys = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_categorys(self, obj):
        return [i.name for i in obj.categorys.all()]
