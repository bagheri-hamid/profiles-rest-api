from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiView = [
            'this is just for test',
            'so what can we say here?!',
            'nothing',
        ]

        return Response({'Message' : 'Hello', 'an ApiView' : an_apiView})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' : 'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method' : 'DELETE'})


class HelloViewSets(viewsets.ViewSet):
    """Test api ViewSets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """returns a hello message"""
        a_viewset = [
        'this is just a test',
        'so ignore this message',
        'just that',
        ]

        return Response({'Message':'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello Mr/Ms {name}'
            return Response({'Message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method' : 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method' : 'DELETE'})
