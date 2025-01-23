from dj_rest_auth.registration.views import RegisterView

from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser, UserProfile
from .serializers import (
    CustomRegisterSerializer,
    CustomUserSerializer,
    UserProfileSerializer,
)


class CustomRegisterView(RegisterView):
    
    serializer_class = CustomRegisterSerializer


class UserProfileUpdateView(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class WorkerListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(custom_role='WORKER')

        service_type = self.request.query_params.get('serviceType', None)
        location = self.request.query_params.get('location', None)

        if service_type:
            queryset = queryset.filter(services__contains=[service_type])
        if location:
            queryset = queryset.filter(city__icontains=location)

        return queryset
