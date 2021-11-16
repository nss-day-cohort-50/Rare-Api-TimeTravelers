# from django.core.exceptions import ValidationError
# from rest_framework import status
# from rest_framework import serializers
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework.serializers import ModelSerializer, BooleanField
# from django.contrib.auth.models import User
# from rarerestapi.models import RareUsers, Posts
# from rest_framework.decorators import action

# class PostView(ViewSet):
#     def create(self, request):
#         author = RareUser.objects.get(user=request.auth.user)
#         post = Posts.objects.get(pk=request.data['gameId'])

#         try:
#             post = Posts.objects.create(
#                 title=title,
#                 organizer=organizer,
#                 publications_date=request.data['date'],
#                 content=request.data['content'],
#                 approved=request.data['approved'],
#                 image_url=request.data['image_url']
#             )
#             event_serializer = EventSerializer(event, context={'request': request})
#             return Response(event_serializer.data, status=status.HTTP_201_CREATED)
#         except ValidationError as ex:
#             return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request):
#         post = Posts.objects.get(user=request.auth.user)
#         events = Event.objects.all()

    
#         for event in events:
#             event.joined = post in event.attendees.all()
#         game = self.request.query_params.get('gameId', None)
#         if game is not None:
#             events = events.filter(game__id=type)

#         serializer = EventSerializer(
#             events, many=True, context={'request': request})
#         return Response(serializer.data)

    
#     def retrieve(self, request, pk):
#         event = Event.objects.get(pk=pk)
#         event_serializer = EventSerializer(event, context={'request': request})
#         return Response(event_serializer.data)

#     def destroy(self, request, pk):
#         event = Event.objects.get(pk=pk)
#         event.delete()

#         return Response(None, status=status.HTTP_204_NO_CONTENT)

#     def update(self, request, pk):
#         post = Posts.objects.get(pk=pk)
#         post.date = request.data['date']
#         post.time = request.data['time']
#         post.description = request.data['description']
#         post.game = Game.objects.get(pk=request.data['gameId'])
#         post.save()

#         return Response(None, status=status.HTTP_204_NO_CONTENT)

#     @action(methods=['post', 'delete'], detail=True)


# class PostSerializer(ModelSerializer):
   
#     class Meta:
#         model = Posts
#         fields = ['user']

