from rest_framework.permissions import BasePermission

class OnlyCandidate(BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type.user_type == 'candidate':
            return True
        return False
    
    