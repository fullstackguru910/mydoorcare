from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from users.models import CustomUser, UserProfile


class CustomRegisterSerializer(RegisterSerializer):
    
    def custom_signup(self, request, user):
        profile_data = {
            'user': user,
        }
        profile_serializer = UserProfileSerializer(data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save(user=user)
        else:
            raise serializers.ValidationError(profile_serializer.errors)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'phone_number', 'address', 'profile_image', 'services']
        extra_kwargs = {
            'profile_image': {'required': False},
        }


class CustomUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'custom_role',
            'profile',
        ]
