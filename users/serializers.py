from dj_rest_auth.registration.serializers import RegisterSerializer

from allauth.account.adapter import get_adapter


class CustomRegisterSerializer(RegisterSerializer):
    pass
