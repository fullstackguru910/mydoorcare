from django.urls import path, include

from .views import (
    BookingCreateAPIView,
)


urlpatterns = [
    path('create/', BookingCreateAPIView.as_view(), name="booking-create"),
]
