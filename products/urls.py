from django.urls import path, re_path, include
from .views import Products, MiscellaneousPages, ProductsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProductsViewSet, basename='prod' )


urlpatterns = [
    path('',include(router.urls))
]

urlpatterns += [
    path('home', Products.as_view(), name='root_path'),
]

urlpatterns += [
    re_path(r'.*', MiscellaneousPages.not_found, name='not_found_path')
]