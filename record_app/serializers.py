from django.forms import ValidationError
from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    categorys = CategorySerializer(many=True, read_only=True)
    set_category = serializers.ListField(write_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        category_model = Category

    def validate_set_category(self, val):
        categorys_queryset = self.Meta.category_model.objects.filter(pk__in=val)
        if categorys_queryset.count() != len(val):
            raise serializers.ValidationError("Неверный список!")
        return categorys_queryset

    def create(self, validated_data):
        categorys_queryset = validated_data.pop('set_category')
        instance = self.Meta.model.objects.create(**validated_data)
        instance.categorys.set(categorys_queryset)
        return instance

    def update(self, instance, validated_data):
        categorys_queryset = validated_data.pop('set_category')
        obj = super().update(instance, validated_data)
        obj.categorys.clear()
        instance.categorys.set(categorys_queryset)
        return obj
