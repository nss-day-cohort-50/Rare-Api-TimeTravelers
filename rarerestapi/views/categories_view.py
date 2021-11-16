from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rarerestapi.models import Categories
from rest_framework import status


class CategoryView(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single category

        Returns:
            Response -- JSON serialized category
        """
        try:
            categories = Categories.objects.get(pk=pk)
            serializer = CategoriesSerializer(categories, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Categories.objects.all()

        serializer = CategoriesSerializer(
            categories, many=True, context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):

        try:
            category = Categories.objects.create(
                label=request.data["label"]
            )
            serializer = CategoriesSerializer(category, context={'request': request})
            return Response(serializer.data)
        
        except ValueError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class CategoriesSerializer(serializers.ModelSerializer):
    """JSON serializer for categories

    Arguments:
        serializers
    """
    class Meta:
        model = Categories
        fields = ('id', 'label')
