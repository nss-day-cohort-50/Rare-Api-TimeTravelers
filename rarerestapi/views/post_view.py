from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, BooleanField
from django.contrib.auth.models import User
from rarerestapi.models import RareUsers, Posts, Categories
from rest_framework.decorators import action

class PostView(ViewSet):
    def create(self, request):
        user = RareUsers.objects.get(user=request.auth.user)
        category = Categories.objects.get(pk=request.data['categoryId'])
        
        try:               
            post = Posts.objects.create(
                user=user,
                title = request.data["title"],
                category = category,
                publication_date=request.data['publicationDate'],
                content=request.data['content'],
                approved=request.data['approved'],
                image_url=request.data['imageUrl']
            )
            post_serializer = PostSerializer(post, context={'request': request})
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        posts = Posts.objects.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)

    
    def retrieve(self, request, pk):
        post = Posts.objects.get(pk=pk)
        post_serializer = PostSerializer(post, context={'request': request})
        return Response(post_serializer.data)

    @action(methods=['GET'], detail=False)
    def myPosts(self, request):
        user = RareUsers.objects.get(user=request.auth.user)

        try:
            post = Posts.objects.filter(user = user)
            post_serializer = PostSerializer(post, many=True, context={'request': request})
            return Response(post_serializer.data)
        except Posts.DoesNotExist:
            return Response(
                {'message': 'Post does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )    

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id']

class PostSerializer(ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Posts
        fields = ['id', 'user', 'title', 'category', 'publication_date', 'approved', 'content', 'image_url']

