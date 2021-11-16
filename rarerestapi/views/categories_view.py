from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rarerestapi.models import Categories


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

class CategoriesSerializer(serializers.ModelSerializer):
    """JSON serializer for categories

    Arguments:
        serializers
    """
    class Meta:
        model = Categories
        fields = ('id', 'label')
