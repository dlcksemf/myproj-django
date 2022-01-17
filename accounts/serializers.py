from typing import Dict

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OriginTokenObtainPairSerializer,
    TokenRefreshSerializer as OriginTokenRefreshSerializer,
)


class TokenObtainPairSerializer(OriginTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Dict:
        token = super().get_token(user)
        token["username"] = user.username
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        return token


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass
