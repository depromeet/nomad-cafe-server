from django.contrib.auth.models import User as Admin
from .models import Cafe, User, Rating, Tag
from rest_framework import serializers


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'id',
            'cafe_id',
            'user_id',
            'tags',
            'create_dt',
            'update_dt',
        ]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = ['url', 'username', 'email', 'groups']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'create_dt',
            'update_dt',
        ]


class CafeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cafe
        fields = [
            'id',
            'data_id',
            'data_type',
            'create_dt',
            'update_dt',
            'data_id',
            'start_hours',
            'end_hours',
            'location',
            'name',
            'brand_name',
            'x',
            'y',
            'parcel_addr',
            'zipcode',
            'phone',
            'road_addr',
            'homepage',
            'img',
            'tags',
        ]