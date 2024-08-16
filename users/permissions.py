#권한 정보를 위한 파일

from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission): #기본적인 권한에 대한걸 상속받아 읽을수만 있는 클래스 하나를 생성
    def has_object_permission(self, request, view, obj): #오브젝트에 대한 권한이 있는지에 대해 확인하는 함수
                            #(리퀘스트, 어떤 뷰인지, 어떤 오브젝트에 대한건지)
        if request.method in permissions.SAFE_METHODS: #데이터를 건드리지 않는 메서드(ex: 읽기전용 같은거)
            return True  #어차피 데이터에 가는 영향이 없으므로 True를 뱉도록 한다.
        return obj.author == request.user #대상object의 소유자와 리퀘스트의 요청자가 같으면 True
    