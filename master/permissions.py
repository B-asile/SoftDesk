from rest_framework import permissions


class Update_what_is_mine(permissions.BasePermission):
    ''''''

    def has_object_permission(self, request, view, obj):
        '''toutes les methodes lecture sont autorisées'''
        if request.method in permissions.SAFE_METHODS:
            '''toutes les methodes lecture sont autorisées'''
            return True
        elif obj.id == request.user_id:
            '''autorisation de modification objects appartenant a utilisateur_identifié'''
            return True
        else:
            return False