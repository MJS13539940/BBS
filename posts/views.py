#from django.shortcuts import render (템플릿 안만들어서 render는 필요없음.)
from rest_framework import viewsets # CRUD 다 가능한게 viewset

from users.models import Profile #쓸 모델
from .models import Post #저장할 모델
from .permissions import CustomReadOnly #
from .serializers import PostSerializer, PostCreateSerializer #


# Create your views here.
#모델과 시리얼라이저를 연결한다.

# <<< >>>
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() #장고 rest_framework 내에서 쿼리셋 등을 다 처리해줌
#    permission_classes = [CustomReadOnly] #권한은 복수적용될 수 있기때문에 리스트형태로 작성
# <<<이부분 문제있으니 나중에 수정>>>


    #시리얼라이저로부터 정보를 읽어옴
    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve': # ModelViewSet 내의 기능
            return PostSerializer #PostSerializer를 통해서 수행하라.
        return PostCreateSerializer #그 외엔 PostCreateSerializer를 통해 수행하라.

    #작업을 수행할 함수(?)
    def perform_create(self, serializer): #시리얼라이저를 전달받음
        profile = Profile.objects.get(user=self.request.user) #프로필의 유저에 대한 정보를 읽어옴
        serializer.save(author=self.request.user, profile=profile) #시리얼라이저에 해당정보를 받아 저장함.

