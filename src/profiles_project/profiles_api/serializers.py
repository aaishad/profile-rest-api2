from rest_framework import serializers

class HelloUserSerializer(serializers.Serializer):
    """serializers for name field for test our APIView"""

    name = serializers.CharField(max_length=10)
