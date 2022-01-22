from rest_framework.permissions import BasePermission

# IsOwner is the custom Permission class explicitly created to verify the owner of the task
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user