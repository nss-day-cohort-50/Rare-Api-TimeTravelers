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
    # def create(self, request):
    #     author = RareUsers.objects.get(user=request.auth.user)
    #     post = Posts.objects.get(pk=request.data['gameId'])

    #     try:               
    #         post = Posts.objects.create(
    #             title = request.data["title"],
    #             user_id = models.IntegerField("RareUsers")
    #             category_id = models.IntegerField("Categories")
    #             publications_date=request.data[]
    #             content=request.data['content'],
    #             approved=request.data['approved'],
    #             image_url=request.data['image_url']
    #         )
    #         post_serializer = PostSerializer(post, context={'request': request})
    #         return Response(post_serializer.data, status=status.HTTP_201_CREATED)
    #     except ValidationError as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        post = Posts.objects.get(user=request.auth.user)
        posts = post.objects.all()

        game = self.request.query_params.get('gameId', None)
        if game is not None:
            posts = posts.filter(game__id=type)

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)

    
    def retrieve(self, request, pk):
        post = Posts.objects.get(pk=pk)
        post_serializer = PostSerializer(post, context={'request': request})
        return Response(post_serializer.data)


class PostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ['user', 'title', 'category', 'publication_date', 'approved', 'content']

