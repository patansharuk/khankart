from django.urls import path, re_path, include
from .views.products import Products, MiscellaneousPages, CreateProduct, UpdateProduct, ViewProduct, DeleteProduct
from .views.swagger import ProductsViewSet, UserViewSet
from .views.carts import Carts
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='prod')
router.register(r'users',UserViewSet, basename='usr')


urlpatterns = [
    path('',include(router.urls))
]

urlpatterns += [
    path('home', Products.as_view(), name='root_path'),
    path('add', CreateProduct.as_view(), name='add_product_path'),
    path('<int:product_id>/change', UpdateProduct.as_view(), name='change_product_path'),
    path('<int:product_id>/show', ViewProduct.as_view(), name="view_product_path"),
    path('<int:product_id>/delete', DeleteProduct.as_view(), name="delete_product_path"),
]

urlpatterns += [
    path('home/cart', Carts.as_view(), name='carts_path'),
]

urlpatterns += [
    re_path(r'.*', MiscellaneousPages.not_found, name='not_found_path')
]