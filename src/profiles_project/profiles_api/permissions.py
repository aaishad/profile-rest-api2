from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit own profile"""

    def has_object_permission(self,request, view, obj):
        """check user is tring to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow user to update own status"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to update their on status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id    
