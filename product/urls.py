from django.urls import path
from product.views import ProductAPIView, CategoryAPIView

urlpatterns = [
    path("product/", ProductAPIView.as_view()),
    path("product/<int:pk>", ProductAPIView.as_view()),
    path("category/", CategoryAPIView.as_view()),
    path("category/<int:pk>", CategoryAPIView.as_view()),
]
