from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}} #Hides password from responses

    def create(self, validated_data):
        return User.objects.create_user(**validated_data) #create_user -> hashes password automatically
