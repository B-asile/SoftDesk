from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from globalapp.models import Projects
from globalapp.serializers import ProjectsSerializers


class ProjectApiView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = ProjectsSerializers
    queryset = Projects.objects.all()
    permission_classes = (IsAuthenticated, )
