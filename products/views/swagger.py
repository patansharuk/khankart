from products.models import Product
from products.serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ModelViewSet, User):
    queryset = User.objects.all()
    serializer_class = UserSerializer