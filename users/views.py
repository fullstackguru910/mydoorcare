from dj_rest_auth.registration.views import RegisterView

from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile
from .serializers import CustomRegisterSerializer, UserProfileSerializer


class CustomRegisterView(RegisterView):
    
    serializer_class = CustomRegisterSerializer


class UserProfileUpdateView(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
