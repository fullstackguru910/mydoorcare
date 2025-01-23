from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('HOME CARE', 'HOME CARE'),
        ('CHILD CARE', 'CHILD CARE'),
        ('ELDER CARE', 'ELDER CARE'),
        ('PET CARE', 'PET CARE'),
    ]
    STATUS_CHOICES = [
        ('PENDING', _('PENDING')),
        ('APPROVED', _('APPROVED')),
        ('COMPLETED', _('COMPLETED')),
        ('CANCELLED', _('CANCELLED')),
        ('FAILED', _('FAILED')),
    ]
    hiring = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='hiring_booking')
    hired = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='hired_booking')
    services = models.JSONField(default=list, blank=True)
    service_details = models.TextField(blank=True, null=True)
    scheduled = models.DateTimeField()
    status = models.CharField(_("status"), max_length=10, choices=STATUS_CHOICES, default='PENDING')
    started = models.DateTimeField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"Booking by {self.hiring.email} - Status: {self.status}"
