from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers

class HelloApiView(APIView):
    """test API Views"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns the list of ApiView features"""
        an_apiview = [
        "Use HTTP methods and functions (GET, POST, PUT, PATCH, DELETE)",
        "Is similar to traditionnal Django Views",
        "Gives you the most control over your application logic",
        "Is mapped manually URLs",
        ]

        return Response({
        'message': 'hello',
        'an_apiview': an_apiview,
        })

    def post(self, request):
        """createnthe hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message': 'put methode'})

    def patch(self, request, pk=None):
        """HAndle a partial update of an object"""
        return Response({'message':'patch methode'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message': 'Delete methode'})




class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer
    """Hello Api ViewSet"""

    def list(self, request):
        """returns the list of ApiView features"""
        an_apiview = [
        "Use HTTP methods and functions (GET, POST, PUT, PATCH, DELETE)",
        "Is similar to traditionnal Django Views",
        "Gives you the most control over your application logic",
        "Is mapped manually URLs",
        ]

        return Response({
        'message': 'hello',
        'an_apiview': an_apiview,
        })

    def create(self, request):
        """createnthe hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message': 'get methode'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message': 'put methode'})

    def partial_update(self, request, pk=None):
        """HAndle a partial update of an object"""
        return Response({'message':'patch methode'})

    def destroy(self, request, pk=None):
        """Delete an object"""
        return Response({'message': 'Delete methode'})
