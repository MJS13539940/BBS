from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics, status #status는 상태에 대한 표시를 담당.
from rest_framework.response import Response #응답을 받는 용도

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer # 시리얼라이저에 만들어둔것들
from .models import Profile
from users.permissions import CustomReadOnly

# Create your views here.



class RegisterView(generics.CreateAPIView):
    #필요한 정보는 쿼리셋에 다 받아옴
    queryset = User.objects.all()
    #RegisterSerializer 의 인스턴스 생성
    serializer_class = RegisterSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request): #포스트를 통해서 토큰의 정보와 상태를 반환
        #리퀘스트가 가진 데이터를 들고와서 변수에 할당
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) #검증 단계
        token = serializer.validated_data #검증이 끝난 데이터를 토큰화

        return Response({'token': token.key}, status=status.HTTP_200_OK)
        #토큰의 정보와 상태를 반환한다.

#class ProfileView(generics.CreateAPIView):
#    queryset= Profile.objects.all()
#    serializer_class = ProfileSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    #프로필 오브젝트가 들고있던걸 전부 쿼리셋에
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #그리고 권한을 위한 permissions.py를 생성.
    permission_class = [CustomReadOnly]



#이 뒤에 urls 생성