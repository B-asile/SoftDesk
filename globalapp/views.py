from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Projects, Contributors, Issues, Comments
from .serializers import ProjectsSerializers, ContributorsSerializers, IssuesSerializers, CommentsSerializers


class ProjectApiView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = ProjectsSerializers
    queryset = Projects.objects.all()
    permission_classes = (IsAuthenticated, )


class ContributorApiView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = ContributorsSerializers
    queryset = Contributors.objects.all()
    permission_classes = (IsAuthenticated,)


class IssueApiView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = IssuesSerializers
    queryset = Issues.objects.all()
    permission_classes = (IsAuthenticated,)


class CommentApiView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = CommentsSerializers
    queryset = Comments.objects.all()
    permission_classes = (IsAuthenticated,)
