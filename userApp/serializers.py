from rest_framework import serializers
from .models import User, UserManager


class AdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

