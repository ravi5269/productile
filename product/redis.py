from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from product.models import *
# from product.serializers import ProductSerializer,CategorySerializer
from django.http import JsonResponse

# CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)


def redis_home(request):
    payload = []
    db = None
    if cache.get('Products'):
        payload = cache.get('Products')
        db ='redis'
    else:
        objs = Product.objects.all()
        
        for obj in objs:
            payload.append(obj.name)
        db = 'postgres'

        cache.set('Products',payload)
        
    return JsonResponse({
        'status':200,
        'db':db,
        'data': payload
    })





























# def get_product(filter_product = None):
#     if filter_product:
#         products = Product.objects.filter(name_contains = filter_product)
#     else:
#         products = Product.objects.all()
#     return products


# def redis_product(request):
#     filter_product = request.GET.get('products')
#     if filter_product:
#         products = get_product



# def get(self, request, pk=None):
#     if pk:
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(
#             {"status": "Success", "data": serializer.data},
#             status=status.HTTP_200_OK,
#         )
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(
#         {"status": "Success", "data": serializer.data}, status=status.HTTP_200_OK
#     )




















# from rest_framework.decorators import api_view
# from django.core.cache import caches
# @api_view(['get'])
# def home(request):
#     payload = []
#     db = None
#     if caches.get('product'):
#         payload = caches.get('product')
#         db = 'redis'
#     else:
#         objs = Product.objects.all()
#         for obj in objs:
#             payload.append(obj.product_name)
#         db = 'postgres'
#         caches.set('product',payload)
#     return Response({
#         'status':200,
#         'db':'postgres',
#         'data':payload
#     })