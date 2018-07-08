from rest_framework.permissions import BasePermission
from .models import User

class IsTeacher(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated() and request.user.role == User.TEACHER

class IsStudent(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated() and request.user.role == User.STUDENT

class IsTestOwner(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated() and request.user.is_test_owner(view.kwargs.get('pk'))
