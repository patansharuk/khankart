from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from ..models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime


class Perm:
    def __init__(self, request):
        self.username = request.user.username
        self.can_view_products = request.user.has_perm(
            'products.view_products')
        self.can_add_products = request.user.has_perm('products.add_products')
        self.can_delete_products = request.user.has_perm(
            'products.delete_products')
        self.can_change_products = request.user.has_perm(
            'products.change_products')


class Products(LoginRequiredMixin, TemplateView):
    def get(self, request):
        user_perm = Perm(request)
        message = ''
        if (user_perm.can_view_products):
            products = Product.objects.all()
        else:
            products = []
            message = 'You dont have permission to view products.'
        return render(request, 'products/index.html', {'products': products, 'message': message, 'user_perm': user_perm})


class CreateProduct(Products):
    def get(self, request):
        product = Product()
        return render(request, 'products/new.html', {'product': product})

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        updated_date = datetime.now().date().strftime('%Y-%m-%d')
        print(updated_date)
        print(type(updated_date))
        product = Product(title=title, description=description,
                          price=price, updated_date=updated_date)
        product.save()
        if (product.id):
            return redirect('root_path')
        else:
            return render(request, 'products/index.html', {})


class UpdateProduct(Products):
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        return render(request, 'products/edit.html', {'product': product})

    def post(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        product.title = request.POST['title']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.updated_date = datetime.now()
        product.save()
        return redirect('root_path')


class ViewProduct(Products):
    def get(self, request, product_id):
        user_perm = Perm(request)
        product = Product.objects.get(pk=product_id)
        current_time = datetime.now()
        return render(request, 'products/show.html', {'product': product, 'user_perm': user_perm, 'current_time': current_time})


class DeleteProduct(Products):
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        product.delete()
        return redirect('root_path')


class MiscellaneousPages:
    def not_found(request):
        return render(request, 'not_found.html', {})
