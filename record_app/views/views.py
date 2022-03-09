from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)

from logging_app.logging_view_mixin import (
    CreateViewLoggigMixin, RetriveLoggingMixin, UpdateLoggingMixin, DestroyLoggingMixin
)

from ..logging_serializers import ProductLogSerializer
from ..forms import ProductForm
from ..models import Product
# Create your views here.


class ProductListView(ListView):
    model = Product
    queryset = model.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('categorys')
        return queryset


class ProductCreateView(CreateViewLoggigMixin, CreateView):
    model = Product
    form_class = ProductForm
    serializer_log_class = ProductLogSerializer
    queryset = model.objects.all()
    success_url = reverse_lazy('product_list')


class ProductDetailView(RetriveLoggingMixin, DetailView):
    model = Product
    serializer_log_class = ProductLogSerializer


class ProductUpdateView(UpdateLoggingMixin, UpdateView):
    model = Product
    form_class = ProductForm
    serializer_log_class = ProductLogSerializer
    queryset = model.objects.all()
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DestroyLoggingMixin, DeleteView):
    model = Product
    serializer_log_class = ProductLogSerializer
    queryset = model.objects.all()
    success_url = reverse_lazy('product_list')
