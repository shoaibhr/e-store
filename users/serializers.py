from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'password', 'phone_number' ]
        extra_kwargs = {"password": {'write_only': True}}
    
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        # Prevent the username and email from being updated
        validated_data.pop('email', None)
        validated_data.pop('username', None)

        # Update other fields
        instance = super().update(instance, validated_data)

        # Handle password update
        if password:
            instance.set_password(password)
            instance.save()

        return instance