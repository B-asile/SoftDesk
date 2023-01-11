from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer
from .models import User
from master.permissions import UpdateOwnProfile


class UserApiRegister(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (UpdateOwnProfile, )


