from django.shortcuts import render
from product.serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category


class ProductAPIView(APIView):
    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "Success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "Not found", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            print(e)
            return Response({})

    def get(self, request, pk=None):
        if pk:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(
                {"status": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(
            {"status": "Success", "data": serializer.data}, status=status.HTTP_200_OK
        )

    def put(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Not found data", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({"message": "Deleted"})


class CategoryAPIView(APIView):
    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "Success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "Not found", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            print(e)
            # return Response({})

    def get(self, request, pk=None):
        if pk:
            product = Category.objects.get(pk=pk)
            serializer = CategorySerializer(product)
            return Response(
                {"status": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        products = Category.objects.all()
        serializer = CategorySerializer(products, many=True)
        return Response(
            {"status": "Success", "data": serializer.data}, status=status.HTTP_200_OK
        )

    def put(self, request, pk=None):
        product = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Not found data", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk=None):
        product = get_object_or_404(Category, pk=pk)
        product.delete()
        return Response({"message": "Deleted"})
