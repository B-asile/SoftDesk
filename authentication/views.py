from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer
from .models import User
from master.permissions import Update_own_profile


class UserApiRegister(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (Update_own_profile, )


