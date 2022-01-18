from typing import Dict

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OriginTokenObtainPairSerializer,
    TokenRefreshSerializer as OriginTokenRefreshSerializer,
)


class TokenObtainPairSerializer(OriginTokenObtainPairSerializer):
    def validate(self, attrs):
        data: Dict = super().validate(attrs)
        data["username"] = self.user.username
        data["first_name"] = self.user.first_name
        data["last_name"] = self.user.last_name
        # TODO : 프로필 이미지 URL
        return data


# JWT Payload 커스텀
# @classmethod
# def get_token(cls, user) -> Dict:
#     token = super().get_token(user)
#     token["username"] = user.username
#     token["first_name"] = user.first_name
#     token["last_name"] = user.last_name
#     return token


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass
