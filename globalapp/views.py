from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Projects, Contributors, Issues, Comments
from .serializers import ProjectsSerializers, ContributorsSerializers, IssuesSerializers, CommentsSerializers


class ProjectApiView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = ProjectsSerializers
    queryset = Projects.objects.all()
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        '''create author_User par default'''
        new_project = serializer.save(author_user_id=self.request.user)
        Contributors.objects.create(user_id=self.request.user, project_id=new_project, permission='author', role='project_owner')
        new_project.contribs.add(self.request.user)
        new_project.save()




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

    def perform_create(self, serializer):
        new_issue = serializer.save(author_user_id=self.request.user,
                                    project_id=get_object_or_404(Projects, pk=self.kwargs['projects_pk'])
                                    )
        new_issue.save()


class CommentApiView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = CommentsSerializers
    queryset = Comments.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        new_comment = serializer.save(author_user_id=self.request.user,
                                    issue_id=get_object_or_404(Issues, pk=self.kwargs['issues_pk'])
                                    )
        new_comment.save()
