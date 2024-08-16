from rest_framework import permissions


#User의 CustomReadOnly 때와 다르게 권한을 케이스별로 다 지정해줘야한다.
class CustomReadOnly(permissions.BasePermission):
    #권한이 있는지 확인하는 함수
    def has_permission(self, request, view): #리퀘스트와 어느 뷰에서 작동할지를 받음.
        if request.method == 'GET': #주소를 통해 접근(=조회)할 경우는 그냥 통과시켜준다.
            return True
        return request.user.is_authenticated #인증이 되었다면 True가 반환될것
    
    #해당하는 오브젝트에 대한 권한을 확인하는 함수
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #데이터를 건드리지 않는 기능이 요청된 경우 True
            return True
        return obj.author == request.user #object의 주인과 리퀘스트의 유저 정보의 일치 여부
    
