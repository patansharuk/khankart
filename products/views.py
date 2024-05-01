from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class Authenticate(TemplateView):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        return redirect('login_path')


class Products(TemplateView):
    def get(self, request):
        products = [1,2,3]
        return render(request, 'index.html', {'products': products})


class MiscellaneousPages:
    def not_found(request):
        return render(request, 'not_found.html', {})
