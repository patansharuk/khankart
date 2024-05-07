from django.urls import path, re_path, include
from .views import Products, MiscellaneousPages, ProductsViewSet, UserViewSet, update_product, view_product, delete_product, new_product, edit_product , add_product
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='prod')
router.register(r'users',UserViewSet, basename='usr')


urlpatterns = [
    path('',include(router.urls))
]

urlpatterns += [
    path('home', Products.as_view(), name='root_path'),
    path('new', new_product, name='new_product_path'),
    path('add', add_product, name='add_product_path'),
    path('<int:product_id>/show', view_product, name="view_product_path"),
    path('<int:product_id>/edit', edit_product, name="edit_product_path"),
    path('<int:product_id>/update', update_product, name='update_product_path'),
    path('<int:product_id>/delete', delete_product, name="delete_product_path"),
]

urlpatterns += [
    re_path(r'.*', MiscellaneousPages.not_found, name='not_found_path')
]