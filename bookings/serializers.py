from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'hiring',
            'hired',
            'services',
            'service_details',
            'scheduled',
            'started',
            'accepted,'
            'status',
            'created',
        ]
        read_only_fields = ['id', 'hiring', 'status', 'started', 'accepted', 'created']
