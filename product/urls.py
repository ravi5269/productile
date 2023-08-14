from django.urls import path
from product.filter import ProductFilterView
from product.views import ProductAPIView, CategoryAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from product.redis import redis_home


urlpatterns = [
    path("product/", ProductAPIView.as_view()),
    path("product/<int:pk>", ProductAPIView.as_view()),
    path("category/", CategoryAPIView.as_view()),
    path("category/<int:pk>", CategoryAPIView.as_view()),
    path("filter/", ProductFilterView.as_view()),
    path("", redis_home),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
