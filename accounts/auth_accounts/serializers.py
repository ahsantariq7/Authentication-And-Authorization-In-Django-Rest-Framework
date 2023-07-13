from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields='__all__'


class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    #password=
    class Meta:
        model=MyUser
        fields=['email','password']
        