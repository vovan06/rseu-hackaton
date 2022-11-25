from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import User


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=256
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')
        read_only_fields = ['token']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=256
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)