from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from globalapp.models import Projects


class Update_own_profile(permissions.BasePermission):
    ''''''

    def has_object_permission(self, request, view, obj):
        '''toutes les methodes lecture sont autorisées'''
        if request.method in permissions.SAFE_METHODS:
            '''toutes les methodes lecture sont autorisées'''
            return True
        elif obj.id == request.user.id:
            '''autorisation de modification objects appartenant a utilisateur_identifié'''
            return True
        else:
            return False
'''
class Update_projects_read(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            for i in obj.contribs.all():
                if i.id == request.user.id:
                    return True, print('contrib ok')
        else:
            return False


class Update_projects_write(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj.author_user_id.id)
        print(request.user.id)
        if obj.author_user_id.id == request.user.id:
            return True, print('check author ok')
        else:
            return False, print('check KO')
'''

class Update_projects(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            for i in obj.contribs.all():
                if i.id == request.user.id:
                    return True
        return obj.author_user_id.id == request.user.id

class Update_issues(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            proj_of_issue=get_object_or_404(Projects, pk=view.kwargs['projects_pk'])
            for i in proj_of_issue.contribs.all():
                if i.id == request.user.id:
                    return True
        return obj.author_user_id.id == request.user.id

class Update_contributors(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        '''authorisation d'acces pour la section contributeurs
        -si user authentifié appartiend à la liste des contributeurs projet authorisation safeMethode
        - si id personne co == id contrib recherché -> droit en écriture
        -si id co==autheur projet -> droit en écriture sur projet+contrib'''
        proj_of_contrib = get_object_or_404(Projects, pk=view.kwargs['projects_pk'])
        if request.method in permissions.SAFE_METHODS:
            for i in proj_of_contrib.contribs.all():
                if i.id == request.user.id:
                    return True, print('sol1')
        elif obj.user_id.id == request.user.id:
            return True, print('sol2')
        elif proj_of_contrib.author_user_id.id == request.user.id:
            return True, print('sol3')

class Update_comments(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        proj_of_contrib = get_object_or_404(Projects, pk=view.kwargs['projects_pk'])
        if request.method in permissions.SAFE_METHODS:
            for i in proj_of_contrib.contribs.all():
                if i.id == request.user.id:
                    return True, print('sol1')
        elif obj.author_user_id.id == request.user.id:
            return True, print('sol2')
        elif proj_of_contrib.author_user_id.id == request.user.id:
            '''author_user_id du projet!'''
            return True, print('sol3')
