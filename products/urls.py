from django.urls import path
from .views import Products

urlpatterns = [
    path('', Products.as_view(), name='root_path'),
]
