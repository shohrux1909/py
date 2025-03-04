from rest_framework import serializers
from .models import Category, Post, Reyting, Banner, Settings,Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =( '__all__')


class ReytingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reyting
        fields = ('__all__')


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('__all__')


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')

