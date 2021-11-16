from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BooleanField 
from rarerestapi.models import RareUsers
from django.contrib.auth.models import User



class RareUserView(ViewSet):
    

    def retrieve(self, request, pk=None):
       
        try:
            rareuser = RareUsers.objects.get(pk=pk)
            serializer = RareUserSerializer(rareuser, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
       
        rareusers = RareUsers.objects.all()

        
        serializer = RareUserSerializer(
            rareusers, many=True, context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        user_id = user.objects.get(user=request.auth.user)
        

        try:
            event = Event.objects.create(
                
                description=request.data['description'],
                date=request.data['date'],
                time=request.data['time']
            )
            event_serializer = EventSerializer(event, context={'request': request})
            return Response(event_serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', "email"]

class RareUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    active = BooleanField(required=False)
    
    class Meta:
        model = RareUsers
        fields = ['id', 'bio', 'profile_image_url', 'created_on', 'active', 'user']
        depth = 1 