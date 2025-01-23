from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RoomViewSet, MessageViewSet, RoomDetailView


router = DefaultRouter()
router.register('rooms', RoomViewSet, basename='room')
router.register('messages', MessageViewSet, basename='message')

urlpatterns = [
    path('test/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    path('', include(router.urls)),
]
