from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response


class Products(LoginRequiredMixin, TemplateView):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'index.html', {'products': products})

    def post(self, request):
        product = Product(title='title', description='this description',
                          price=100, updated_date='2012-01-01')
        product.save()
        if (product.id):
            return redirect('root_path')
        else:
            return render(request, 'index.html', {})


class MiscellaneousPages:
    def not_found(request):
        return render(request, 'not_found.html', {})


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})