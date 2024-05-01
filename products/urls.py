from django.urls import path, re_path
from .views import Products, Login, Logout, MiscellaneousPages

urlpatterns = [
    path('', Products.as_view(), name='root_path'),
]

urlpatterns += [
    path('login', Login.as_view(), name='login_path'),
    path('logout', Logout.as_view(), name='logout_path'),
]

urlpatterns += [
    re_path(r'.*',MiscellaneousPages.not_found, name='not_found_path')
]