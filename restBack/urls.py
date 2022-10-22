from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/get_exponents', ExponentView.as_view(), name='get_exponents'),
    path('api/v1/exponent/<int:pk>', exponent_detail, name='get_exponents'),
]
