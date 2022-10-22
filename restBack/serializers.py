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
    class Meta:
        model = Exponent
        exclude = ['title', 'meta_keywords', 'meta_description', 'logo', 'main_picture', 'import_substitution',
                   'publications', 'description']
