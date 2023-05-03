from rest_framework import serializers, exceptions
from .models import Product, Category, Cart, Brand, User, Address
import re


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password_validator = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*_-]).{8,}$")
    PASSWORD_HELP_TEXT = 'Password must be at least eight characters long with at least one uppercase, ' \
                         'lowercase, number & symbol (#?!@$%^&*_-)'

    def validate(self, attrs):
        password = attrs.get('password')
        if not self.password_validator.search(password):
            raise exceptions.ValidationError(self.PASSWORD_HELP_TEXT)
        return attrs

    class Meta:
        model = User
        fields = '__all__'


class UserSerializerForGet(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ('total_price',)


class CartSerializerForGet(serializers.ModelSerializer):
    products = serializers.StringRelatedField(source='products.name')

    class Meta:
        model = Cart
        fields = '__all__'





