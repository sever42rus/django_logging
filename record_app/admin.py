from django.contrib import admin
from logging_app.logging_admin_mixin import (
    CreateLogModelAdminMixin,
    RetriveLogModelAdminMixin,
    UpdateLogModelAdminMixin,
    DestroyLogModelAdminMixin

)
from .models import Product, Category
from .logging_serializers import ProductLogSerializer, CategoryLogSerializer


@admin.register(Product)
class ProductAdmin(CreateLogModelAdminMixin, RetriveLogModelAdminMixin,
                   UpdateLogModelAdminMixin, DestroyLogModelAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'price',)
    serializer_log_class = ProductLogSerializer
    filter_horizontal = ('categorys',)


@admin.register(Category)
class CategoryAdmin(CreateLogModelAdminMixin, RetriveLogModelAdminMixin,
                    UpdateLogModelAdminMixin, DestroyLogModelAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name',)
    serializer_log_class = CategoryLogSerializer
