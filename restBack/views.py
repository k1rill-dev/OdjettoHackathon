from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import *


class ExponentView(ListCreateAPIView):
    queryset = Exponent.objects.all()
    serializer_class = ExponentSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ExponentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Exponent.objects.all()
    serializer_class = ExponentSerializer

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CaseView(ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class CaseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class PartnerView(ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class PartnerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer



class ReviewView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class PublicationView(ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class PublicationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class LocationView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class LocationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CatalogView(ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class CatalogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer