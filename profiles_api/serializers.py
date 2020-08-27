from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ serializes the name field for esting our APIView"""

    name = serializers.CharField(max_length=10)
