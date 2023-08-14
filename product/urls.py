from django.urls import path
from product.filter import ProductFilterView
from product.views import ProductAPIView, CategoryAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.urlpatterns import format_suffix_patterns
from product.redis import manage_items, manage_item

urlpatterns = [
    path("product/", ProductAPIView.as_view()),
    path("product/<int:pk>", ProductAPIView.as_view()),
    path("category/", CategoryAPIView.as_view()),
    path("category/<int:pk>", CategoryAPIView.as_view()),
    path("filter/", ProductFilterView.as_view()),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("redis/", manage_items, name="items"),
    path("redis/<slug:key>", manage_item, name="single_item"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
