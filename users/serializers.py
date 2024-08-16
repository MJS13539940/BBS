from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate #인증을 위함

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator   

from .models import Profile #프로필에 대한 모델


#회원등록
class RegisterSerializer(serializers.ModelSerializer):
    #유저네임은 자체 기능으로 반드시 받아 확인하게 되어있음.
    #그래서 그 외의 항목을 확인하는 코드를 쓴다.
    email = serializers.EmailField(
        required=True, #필수요소 요구
        validators=[UniqueValidator(queryset=User.objects.all())] #쿼리셋 안에 User의 정보를 받아둔다.
    )
    password = serializers.CharField(
        write_only=True,  #읽기 불가능하게함(누출방지)
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        write_only=True, 
        required=True
    )
    
    #정보들을 관리하기 위헤 meta를 작성한다.
    class Meta:
        model = User    #유저 모델 등록
        fields = ('username', 'password', 'password2', 'email') #필드 4개를 등록


    #메서드 작성
    def validate(self, data):
        if data['password'] != data['password2']:
            #잘못입력한 비번은 재확인시킴
            raise serializers.ValidationError(
                {'password': {"Password fields didn't match."}}
            )
        return data
    
    def create(self, validated_data): #validate를 통과한 정보만 받게될 것
        #유저 인스턴스 생성
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        #토큰 생성
        token = Token.objects.create(user=user) #유저정보를 기반으로 토큰생성
        print('---------created token: ', token) #생성된거 확인용

        return user
    

#로그인
class LoginSerializer(serializers.Serializer): #모델에 한정되어 데이터를 읽고 쓰고하는게 아니라서 ModelSerializer를 안쓴다.
    #인증 시 쓰는건 주로 아이디, 비번.
    username = serializers.CharField(required=True) #필수입력
    password = serializers.CharField(required=True, write_only=True) #쓰기만 가능

    def validate(self, data):
        user = authenticate(**data) #키워드로 구성된 여러개의 파라미터를 받음

        if user: #user에 정상적인 데이터가 들어와서 True가 되면 토큰을 발행
            token = Token.objects.get(user=user)
            return token
        
        # 토큰생성에 실패한 경우
        raise serializers.ValidationError(
            {'error': "Unable to log in with provided credentials."}
        )
    
#프로필
class ProfileSerializer(serializers.ModelSerializer): #profile에 해당하는 모델만 쓰므로 ModelSerializer
    class Meta: #정보 관리용
        model = Profile
        fields = ('nickname', 'position', 'subject')