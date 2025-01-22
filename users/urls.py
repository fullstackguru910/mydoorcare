from django.urls import path, include

from .views import (
    CustomRegisterView,
    UserProfileUpdateView,
    WorkerListAPIView,
)


urlpatterns = [
    path('', include('dj_rest_auth.urls')),

    path('register/', CustomRegisterView.as_view(), name="user-create"),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),

    path('workers/', WorkerListAPIView.as_view(), name='worker-list'),

]
