from rest_framework import permissions


class IsAuthenticatedOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        else:
            return bool(request.user and request.user.is_staff)
        

class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        else:
            return bool(request.user and request.user.is_staff)