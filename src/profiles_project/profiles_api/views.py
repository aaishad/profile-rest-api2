from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, format=None):
        """Resturn a list of Api View"""

        an_apiview = [
            'usese http method as function (get,post,put,pacth,delete)',
            'its is similer to traditional django view',
            'gives you the most control over your logic',
            'its mapped to manual to urls'
        ]

        return Response({'massage':'Hello!','APIView':an_apiview})
