from django.db import models
from geo.models import Country, State, District
# Create your models here.


class Category(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Brand(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    units = models.CharField(max_length=10)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    mail = models.EmailField()
    password = models.CharField()
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Address(models.Model):
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    postal_code = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Addresses'

class Cart(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

