from rest_framework import serializers

from users.serializers import ProfileSerializer
from .models import Post

# Nested Serializer 사용해야함 = 시리얼라이저 역할을 상황에 따라 나누는것


class PostSerializer(serializers.ModelSerializer):
    #프로필 정보 가져오기
    profile = ProfileSerializer(read_only=True) #게시글에 쓸 프로필정보는 수정할 일이 없으므로 readonly

    class Meta: #정보를 저장하기 위한 메타클래스
        model = Post
        fields = ('pk', 'profile', 'title', 'body', 'image', 'published_date', 'likes')


#위의 정보들을 받아서 처리할 클래스
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'image')
    