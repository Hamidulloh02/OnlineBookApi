from .serializers import PostSerializer, UserSerializer,CategorySerializer,ContributorSerializers
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics
from .models import Post,Category,Video,Contributor
from .permission import IsAuthorOrReadOnly


from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend,FilterSet,CharFilter
from django.views.generic.list import ListView
# Create your views here.
#Post________________________________________________
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ['category']
    search_fields = ['id','title']

class PostListAPIView(generics.ListAPIView,generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ['category']
    search_fields = ['id','title']
class SingleListAPIView(generics.ListAPIView,generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SearchListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ['category']
    search_fields = ['id','title']

class FilterListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_active=True).order_by('-id')
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ['category']
    search_fields = ['category__name','id']
#Category______________________________________________
class CategoryListAPIView(generics.ListAPIView,generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.filter(is_active=True).order_by('-id')
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ['title']

#Users__________________________________________________
# class UserViewSet(ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

#Contributor_____________________________________________

class ContributorListView(generics.ListAPIView,generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializers