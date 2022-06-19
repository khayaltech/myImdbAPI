from email import message
from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      return bool(request.user and request.user.is_staff)
    
class ReviewUserOrReadOnly(permissions.BasePermission):
  message='Only author of review can edit!'
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      return obj.reviewer==request.user or request.user.is_staff
   

  
