#권한 정보를 위한 파일

from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission): #읽을수만 있는 클래스 하나를 생성
    def has_object_permission(self, request, view, obj): #권한이 있는지에 대해 확인하는 함수
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user #소유자와 요청자가 같으면 True