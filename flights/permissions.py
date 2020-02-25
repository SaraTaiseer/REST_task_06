from rest_framework.permissions import BasePermission
from datetime import date
class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.user.is_staff or request.user == obj.user:
            return True
        return False

class modifyBooking(BasePermission):
    def has_object_permission(self,request,view,obj):
        days =( obj.date - date.today()).days
        if days > 3 :
            return True
        return False
