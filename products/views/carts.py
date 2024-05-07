from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from products.models import Cart


class Carts(LoginRequiredMixin, TemplateView):
    def get(self, request):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        print(cart_items)
        return render(request, 'carts/index.html', {'cart_items': cart_items})

    def post(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        return redirect('carts_path')