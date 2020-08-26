from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test API Views"""

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
