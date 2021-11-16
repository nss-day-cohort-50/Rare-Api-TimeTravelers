from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, BooleanField
from django.contrib.auth.models import User
from rarerestapi.models import Reactions
from rest_framework.decorators import action

class ReactionView(ViewSet):
    def create(self, request):
        label = Reactions.objects.get()
        image_url = Reactions.objects.get()

        try:
            reaction = Reactions.objects.create(
                label=label,
                image=image_url,
            )
            reaction_serializer = ReactionSerializer(reaction, context={'request': request})
            return Response(reaction_serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        reactions = Reactions.objects.all()

    
  

        serializer = ReactionSerializer(
            reactions, many=True, context={'request': request})
        return Response(serializer.data)

    
    def retrieve(self, request, pk):
        reaction = Reactions.objects.get(pk=pk)
        reaction_serializer = ReactionSerializer(reaction, context={'request': request})
        return Response(reaction_serializer.data)

    def destroy(self, request, pk):
        event = Reactions.objects.get(pk=pk)
        event.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        reaction = Reactions.objects.get(pk=pk)
        reaction.date = request.data['label']
        reaction.time = request.data['imageUrl']
        reaction.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    



class ReactionSerializer(ModelSerializer):
    class Meta:
        model = Reactions
        fields = ('label', 'image_url')


