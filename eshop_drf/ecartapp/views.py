from django.shortcuts import render
from rest_framework.permissions import SAFE_METHODS
from .models import Category, Brand, Product, User, Address, Cart
from .serializing import CategorySerializer, BrandSerializer, ProductSerializer, UserSerializer, \
    UserSerializerForGet, AddressSerializer, CartSerializer, CartSerializerForGet
from rest_framework import viewsets

# Create your views here.


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerForGet

    def get_serializer_class(self):
        serializer = self.serializer_class
        if self.request.method not in SAFE_METHODS:
            serializer = UserSerializer
        return serializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializerForGet

    def get_serializer_class(self):
        serializer = self.serializer_class
        if self.request.method not in SAFE_METHODS:
            serializer = CartSerializer
        return serializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        quantity = data.get('quantity')
        products = data.get('products')

        price = products.price_per_unit * quantity
        serializer.save(total_price=price)

    def perform_update(self, serializer):
        data = serializer.validated_data
        quantity = data.get('quantity')
        products = data.get('products')

        price = products.price_per_unit * quantity
        serializer.save(total_price=price)






