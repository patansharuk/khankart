from django.urls import path, re_path
from .views import Products, MiscellaneousPages

urlpatterns = [
    path('', Products.as_view(), name='root_path'),
]

urlpatterns += [
    re_path(r'.*', MiscellaneousPages.not_found, name='not_found_path')
]
