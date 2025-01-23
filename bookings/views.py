from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import BookingSerializer

class BookingCreateAPIView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(hiring=self.request.user)
