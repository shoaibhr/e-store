from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone_number' ]
        extra_kwargs = {"password": {'write_only': True}}
    
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        # Remove the email field from the validated_data to prevent it from being updated
        validated_data.pop('email', None)
        
        # Call the parent update method with the remaining fields
        return super().update(instance, validated_data)