from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, BooleanField
from django.contrib.auth.models import User
from rarerestapi.models import Tags
from rest_framework.decorators import action

class TagView(ViewSet):
    def create(self, request):
        label = request.data["label"]
        

        try:
            tag = Tags.objects.create(
                label=label
            )
            tag_serializer = TagSerializer(tag, context={'request': request})
            return Response(tag_serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        tags = Tags.objects.all()

        serializer = TagSerializer(
            tags, many=True, context={'request': request})
        return Response(serializer.data)

    
    def retrieve(self, request, pk):
        tag = Tags.objects.get(pk=pk)
        tag_serializer = TagSerializer(tag, context={'request': request})
        return Response(tag_serializer.data)

    def destroy(self, request, pk):
        event = Tags.objects.get(pk=pk)
        event.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        tag = Tags.objects.get(pk=pk)
        tag.date = request.data['label']
        tag.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    



class TagSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'label')


