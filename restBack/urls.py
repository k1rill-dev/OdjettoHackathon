from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/exponents', ExponentView.as_view(), name='get_exponents'),
    path('api/v1/exponent/<int:pk>', ExponentDetailView.as_view(), name='exponent'),
    path('api/v1/categories', CategoryView.as_view(), name='get_cats'),
    path('api/v1/category/<int:pk>', CategoryDetailView.as_view(), name='category'),
    path('api/v1/products', ProductView.as_view(), name='get_products'),
    path('api/v1/product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('api/v1/cases', CaseView.as_view(), name='get_cases'),
    path('api/v1/case/<int:pk>', CaseDetailView.as_view(), name='case'),
    path('api/v1/partners', PartnerView.as_view(), name='get_partners'),
    path('api/v1/partner/<int:pk>', PartnerDetailView.as_view(), name='partner'),
    path('api/v1/reviews', ReviewView.as_view(), name='get_reviews'),
    path('api/v1/review/<int:pk>', ReviewDetailView.as_view(), name='review'),
    path('api/v1/publucations', PublicationView.as_view(), name='get_publucations'),
    path('api/v1/publucation/<int:pk>', PublicationDetailView.as_view(), name='publucation'),
    path('api/v1/locations', LocationView.as_view(), name='get_locs'),
    path('api/v1/location/<int:pk>', LocationDetailView.as_view(), name='locations'),
]
