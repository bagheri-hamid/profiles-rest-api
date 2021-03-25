from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiView = [
            'this is just for test',
            'so what can we say here?!',
            'nothing',
        ]

        return Response({'Message' : 'Hello', 'an ApiView' : an_apiView})
