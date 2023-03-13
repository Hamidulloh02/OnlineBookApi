from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Category,Video,Contributor




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','poster')
class ContributorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('id','author','audio')

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'bio', 'created_at','category')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = ('video_title','video_link')