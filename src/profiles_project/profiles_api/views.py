from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloUserSerializer

    def get(self, request, format=None):
        """Resturn a list of Api View"""

        an_apiview = [
            'usese http method as function (get,post,put,pacth,delete)',
            'its is similer to traditional django view',
            'gives you the most control over your logic',
            'its mapped to manual to urls'
        ]

        return Response({'massage':'Hello!','APIView':an_apiview})

    def post(self, request):
        """Create Hello massage with a name"""

        serializer = serializers.HelloUserSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            massage = 'Hello {0}'.format(name)
            return Response({'massage':massage})
        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handle Updating a Object"""
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Handle parial update data"""
        return Response({'massage':'patch'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'massage':'patch'})


class HelloViewSet(viewsets.ViewSet):
    """test viewset"""

    serializer_class = serializers.HelloUserSerializer

    def list(self, request):
        """ list out all object"""
        a_viewset = [
            'Uses action (list, create, reterive, update, partial_update)',
            'Automatically maps to URLS using Router',
            'More Functiollity With Less code'
        ]
        return Response({"massage":"Hello","a_viewset":a_viewset})

    def create(self, request):
        """create a new hello page"""

        serializer = serializers.HelloUserSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            massage = 'Hello {0}'.format(name)

            return Response({'massage':massage})
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handling getting object by its id"""
        return Response({'http_method':'Get'})

    def update(self, request, pk=None):
        """handles update an object"""
        return Response({'http_method':'Put'})

    def partial_update(self, request, pk=None):
        """Handle update partial data"""
        return Response({"http_method":"patch"})

    def destroy(self, request, pk=None):
        """Handle delete data"""
        return Response({"http_method":"Delete"})


class UserProfileViewset(viewsets.ModelViewSet):
    """Handles Creating. creating and update profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
