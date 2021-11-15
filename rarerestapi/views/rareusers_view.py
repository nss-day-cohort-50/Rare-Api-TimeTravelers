from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rarerestapi.models import RareUsers


class RareUserView(ViewSet):
    

    def retrieve(self, request, pk=None):
       
        try:
            rareusers = RareUsers.objects.get(pk=pk)
            serializer = RareUserSerializer(rareuser, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
       
        rareusers = RareUsers.objects.all()

        
        serializer = RareUserSerializer(
            rareusers, many=True, context={'request': request})
        return Response(serializer.data)

class RareUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RareUsers
        fields = ('id', 'bio', 'created', 'active', 'userId')