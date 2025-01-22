from django.urls import path, include

from .views import CustomRegisterView, UserProfileUpdateView


urlpatterns = [
    path('', include('dj_rest_auth.urls')),

    path('register/', CustomRegisterView.as_view(), name="user-create"),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),

]
