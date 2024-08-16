from rest_framework import serializers

from users.serializers import ProfileSerializer
from .models import Post, Comment



#댓글기능
class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'profile', 'post', 'text')

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'text')



# Nested Serializer 사용해야함 = 시리얼라이저 역할을 상황에 따라 나누는것
#글쓰기 기능
class PostSerializer(serializers.ModelSerializer):
    #프로필 정보 가져오기
    profile = ProfileSerializer(read_only=True) #게시글에 쓸 프로필정보는 수정할 일이 없으므로 readonly
    comments = CommentSerializer(many=True, read_only=True) #글 쓸 때 댓글을 같이 보여주기 위함

    class Meta: #정보를 저장하기 위한 메타클래스
        model = Post
        fields = ('pk', 'profile', 'title', 'body', 'image', 'published_date', 'likes')


#위의 정보들을 받아서 처리할 클래스
class PostCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False) #이미지필드를 만들어주고 url을 쓴다. 필수는 아니다.
    
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'image')
    