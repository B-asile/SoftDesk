from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Projects, Contributors, Issues, Comments
from .serializers import ProjectsSerializers, ContributorsSerializers, IssuesSerializers, CommentsSerializers
from master.permissions import UpdateOwnProfile, UpdateProjects, UpdateIssues, UpdateContributors, UpdateComments


class ProjectApiView(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializers
    queryset = Projects.objects.all()
    permission_classes = (
        IsAuthenticated,
        UpdateProjects,
    )

    def perform_create(self, serializer):
        """Par default le créateur d'un projet est ajouté dans les contributeurs du projet"""
        new_project = serializer.save(author_user_id=self.request.user)
        Contributors.objects.create(
            user_id=self.request.user,
            project_id=new_project,
            permission='author',
            role='project_owner'
        )
        new_project.contribs.add(self.request.user)
        new_project.save()

    def get_queryset(self):
        """Affiche tous les projets dans lesquels utilisateur est contribs"""
        return Projects.objects.filter(contribs=self.request.user)


class ContributorApiView(viewsets.ModelViewSet):
    serializer_class = ContributorsSerializers
    queryset = Contributors.objects.all()
    permission_classes = (
        IsAuthenticated,
        UpdateContributors,
    )

    def perform_create(self, serializer):
        """Récupération project_id pour ajout par default"""
        do_not_change_project_id = serializer.save(project_id=get_object_or_404(
            Projects, pk=self.kwargs['projects_pk'])
        )
        do_not_change_project_id.save()

    def get_queryset(self):
        """Affiche tout les contibs du project_id"""
        return Contributors.objects.filter(project_id=get_object_or_404(
            Projects, pk=self.kwargs['projects_pk'])
        )


class IssueApiView(viewsets.ModelViewSet):
    serializer_class = IssuesSerializers
    queryset = Issues.objects.all()
    permission_classes = (
        IsAuthenticated,
        UpdateIssues,
    )

    def perform_create(self, serializer):
        """Par default création issue avec author_user_id"""
        new_issue = serializer.save(
            author_user_id=self.request.user,
            project_id=get_object_or_404(
                Projects, pk=self.kwargs['projects_pk'])
        )
        new_issue.save()

    def get_queryset(self):
        """Affiche les issues correspondant au projet"""
        return Issues.objects.filter(project_id=get_object_or_404(
            Projects, pk=self.kwargs['projects_pk'])
        )


class CommentApiView(viewsets.ModelViewSet):
    serializer_class = CommentsSerializers
    queryset = Comments.objects.all()
    permission_classes = (
        IsAuthenticated,
        UpdateComments
    )

    def perform_create(self, serializer):
        '''Par default création commentaire avec author_user_id'''
        new_comment = serializer.save(author_user_id=self.request.user,
                                      issue_id=get_object_or_404(
                                          Issues, pk=self.kwargs['issues_pk'])
                                      )
        new_comment.save()

    def get_queryset(self):
        '''Retourne les comments liés à une issue'''
        return Comments.objects.filter(issue_id=get_object_or_404(
            Issues, pk=self.kwargs['issues_pk'])
        )
