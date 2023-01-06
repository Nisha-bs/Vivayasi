from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(ModelSerializer):
    _id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['_id', 'username', 'email', 'fullname']

    def get__id(self, userInstance):
        _id = userInstance.id

        return _id


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['_id', 'username', 'email', 'fullname', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)