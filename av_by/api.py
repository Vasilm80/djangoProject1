
from rest_framework import viewsets, permissions
from .serializers import *

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CitySerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('-data_create')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

    def NewUser(self, request, newUser):
        if request.method == 'POST':
            user_phone = request.data.get(newUser.phone)
            user_name = request.data.get(newUser.name)
            user_password = request.data.get(newUser.password)
            user = User.objects.get_or_create(name = user_name, phone = user_phone, password = user_password )

            print(user_name)
            print(user)

