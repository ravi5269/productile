from django.conf import settings

# from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from product.models import *
from django.http import JsonResponse

# CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)


def redis_home(request):
    pass
    payload = []
    db = None
    if cache.get("Products"):
        payload = cache.get("Products")
        db = "redis"
    else:
        objs = Product.objects.all()

        for obj in objs:
            payload.append(obj.name)
        db = "postgres"

        cache.set("Products", payload)

    return JsonResponse({"status": 200, "db": db, "data": payload})
