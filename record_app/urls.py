from django.urls import path
from .views import views

urlpatterns = [
    path(
        '',
        views.ProductListView.as_view(),
        name='product_list'
    ),
    path(
        'create-product/',
        views.ProductCreateView.as_view(),
        name='product_create'
    ),
    path(
        'detail-product/<int:pk>/',
        views.ProductDetailView.as_view(),
        name='product_detail'
    ),
    path(
        'update-product/<int:pk>/',
        views.ProductUpdateView.as_view(),
        name='product_update'
    ),
    path(
        'delete-product/<int:pk>/',
        views.ProductDeleteView.as_view(),
        name='product_delete'
    ),
]
