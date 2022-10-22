from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        User.objects.create(user=user, **profile_data)
        return user


class ExponentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Exponent.objects.create(**validated_data)

    class Meta:
        model = Exponent
        exclude = ['title', 'meta_keywords', 'meta_description', 'logo', 'main_picture', 'import_substitution',
                   'description']


class CategorySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product
        exclude = ['picture', 'video', 'tags', 'is_published']


class CaseSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Case.objects.create(**validated_data)

    class Meta:
        model = Case
        exclude = ['html', 'url_video', 'is_published']


class PartnerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Partner.objects.create(**validated_data)

    class Meta:
        model = Partner
        exclude = ['logo']


class ReviewSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    class Meta:
        model = Review
        exclude = ['picture']


class PublicationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Publication.objects.create(**validated_data)

    class Meta:
        model = Publication
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    class Meta:
        model = Location
        fields = '__all__'
