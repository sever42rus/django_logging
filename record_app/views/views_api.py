from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from logging_app.logging_apiview_mixin import (
    CreateAPILoggingMixin,
    RetrieveUpdateDestroyAPILoggingMixin
)
from ..serializers import ProductSerializer
from ..logging_serializers import ProductLogSerializer
from ..models import Product


class ProductCreateApiView(CreateAPILoggingMixin, CreateAPIView):
    model = Product
    serializer_class = ProductSerializer
    serializer_log_class = ProductLogSerializer


class ProductRetriveUpdateDestrpyAPIView(RetrieveUpdateDestroyAPILoggingMixin, RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer
    serializer_log_class = ProductLogSerializer
    queryset = model.objects.all()
