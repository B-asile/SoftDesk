from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from globalapp.models import Projects


class UpdateOwnProfile(permissions.BasePermission):
    """
    Accès lecture liste des utilisateurs pour tous les utilisateurs
    Accès en écriture pour son propre profile utilisateur
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif obj.id == request.user.id:
            return True
        else:
            return False


class UpdateProjects(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Accès en lecture aux contributeurs d'un projet
        Accès en écriture à l'auteur d'un projet
        """
        if request.method in permissions.SAFE_METHODS:
            for i in obj.contribs.all():
                if i.id == request.user.id:
                    return True
        return obj.author_user_id.id == request.user.id


class UpdateIssues(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Accès en lecture aux contributeurs d'une issue
        Accès en écriture à l'auteur d'une issue
        """
        if request.method in permissions.SAFE_METHODS:
            proj_of_issue = get_object_or_404(Projects, pk=view.kwargs['projects_pk'])
            for i in proj_of_issue.contribs.all():
                if i.id == request.user.id:
                    return True
        return obj.author_user_id.id == request.user.id


class UpdateContributors(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Accès en lecture a la liste des contributeurs du projet
        Accès en écriture à l'auteur d'un projet
        """
        proj_of_contrib = get_object_or_404(Projects, pk=view.kwargs['projects_pk'])
        if request.method in permissions.SAFE_METHODS:
            for i in proj_of_contrib.contribs.all():
                if i.id == request.user.id:
                    return True
        elif obj.user_id.id == request.user.id:
            return True
        elif proj_of_contrib.author_user_id.id == request.user.id:
            return True


class UpdateComments(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Accès en lecture a la liste des commentaires du projet
        Accès en écriture à l'auteur d'un commentaire
        """
        proj_of_contrib = get_object_or_404(Projects, pk=view.kwargs['projects_pk'])
        if request.method in permissions.SAFE_METHODS:
            for i in proj_of_contrib.contribs.all():
                if i.id == request.user.id:
                    return True
        elif obj.author_user_id.id == request.user.id:
            return True
        elif proj_of_contrib.author_user_id.id == request.user.id:
            return True
