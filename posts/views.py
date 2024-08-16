#from django.shortcuts import render (템플릿 안만들어서 render는 필요없음.)
from django_filters.rest_framework import DjangoFilterBackend #가끔 순서 에러가 날 때가 있음. 다른걸 참조하는 경우는 밑으로 보내는게 좋음
from rest_framework import viewsets # CRUD 다 가능한게 viewset

from rest_framework.decorators import api_view, permission_classes #좋아요 기능 용도
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status

from users.models import Profile #쓸 모델
from .models import Post, Comment #저장할 모델, 댓글모델
from .permissions import CustomReadOnly #
from .serializers import PostSerializer, PostCreateSerializer, CommentSerializer, CommentCreateSerializer


# Create your views here.
#모델과 시리얼라이저를 연결한다.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() #장고 rest_framework 내에서 쿼리셋 등을 다 처리해줌
#    permission_classes = [CustomReadOnly] #권한은 복수적용될 수 있기때문에 리스트형태로 작성
# <<<이부분 문제있으니 나중에 수정>>>
    filter_backends = [DjangoFilterBackend] #필터 적용
    filterset_fields = ['author', 'likes'] #필터를 적용하려는 필드

    #시리얼라이저로부터 정보를 읽어옴
    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve': # ModelViewSet 내의 기능
            return PostSerializer #PostSerializer를 통해서 수행하라.
        return PostCreateSerializer #그 외엔 PostCreateSerializer를 통해 수행하라.

    #작업을 수행할 함수(?)
    def perform_create(self, serializer): #시리얼라이저를 전달받음
        profile = Profile.objects.get(user=self.request.user) #프로필의 유저에 대한 정보를 읽어옴
        serializer.save(author=self.request.user, profile=profile) #시리얼라이저에 해당정보를 받아 저장함.

#데코레이터 적용
@api_view(['GET'])
@permission_classes(([IsAuthenticated]))
def like_post(request, pk): #누가
    #pk에 해당하는 포스트를 읽는다
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all(): 
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return Response({'status': 'ok'})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    #

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return CommentSerializer
        return CommentCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)

        