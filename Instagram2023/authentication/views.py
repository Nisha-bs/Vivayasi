from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['POST'])
def register_user(request):
    register_data = request.data

    new_user = CustomUser.objects.create(
            fullname = register_data['fullname'],
            username = register_data['username'],
            email = register_data['email'],
            password = make_password(register_data['password'])
        )
    
    serilizer = UserSerializerWithToken(new_user)

    return Response(serilizer.data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
