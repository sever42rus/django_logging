from django.urls import path
from .views import views_api

urlpatterns = [
    path(
        'product-create/',
        views_api.ProductCreateApiView.as_view()
    ),
    path(
        'product-retrivre-update-destroy/<int:pk>/',
        views_api.ProductRetriveUpdateDestrpyAPIView.as_view()
    ),
]
