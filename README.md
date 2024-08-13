# 게시판 기능 구현

------------------------------------

## 기능

![초안](https://github.com/user-attachments/assets/6a3f77a4-be5a-48e6-a19f-0164cc2704f9)


## 세팅

+ 가상환경 설정, 장고 및 DRF 설치

+ django-admin startproject board .

+ python manage.py startapp users

+ setting.py 수정

![1](https://github.com/user-attachments/assets/ef56432c-c808-4c96-b4e6-1bf1c4d07db9)
![2](https://github.com/user-attachments/assets/c607aa12-498c-4805-addc-090def7ac1e7)
![3](https://github.com/user-attachments/assets/ba2fd8f5-e0ad-4da8-b379-a25724e44eee)

## Serializer

+ 회원가입 기능을 만들기 위해 Usename(ID), email, password를 받기로 함.

+ Username은 User모델에서 자체 제공

+ email, password, password2(입력 확인용)을 받기로 한다.

![4](https://github.com/user-attachments/assets/f68407ce-d6eb-405c-876f-11f253eda37d)
![5](https://github.com/user-attachments/assets/fd876c76-0d9c-41c4-a0ba-e686899d768b)


## View

+ 참고사항

generics.CreateAPIView는 CreateModelMixin과 GenericAPIView를 상속받음

CreateModelMixin은 POST 메서드에 대한 .create(self, request, *args, **kwargs) 메서드를 제공

GenericAPIView는 이 믹스인과 함께 동작하여 실제 HTTP 메서드(POST)를 해당 동작(create)에 매핑함.

즉, 별도의 코드 없이 CreateAPIView를 통해 기능을 구현

![6](https://github.com/user-attachments/assets/07ac2043-5241-4981-a21b-91dc0643e59b)



## URL

![7](https://github.com/user-attachments/assets/50393222-5610-4519-8eb4-ae083ac76b13)
![8](https://github.com/user-attachments/assets/88c328db-cefc-41ce-b960-057beb38e1b3)


## Migration & Runserver

+ 기능 테스트 수행

+ Superuser 통해서 생성한 계정 정보를 확인함.

------------------------------------

## Login 기능 추가
+ Serializer, View, URL 순서로 다시 작성

## Serializer

![9](https://github.com/user-attachments/assets/4af51dcf-1975-46ed-ae9a-0ba0884ffe0c)
![10](https://github.com/user-attachments/assets/5f5e6ff5-3a47-47e4-8831-69389c961e2a)

## View

![11](https://github.com/user-attachments/assets/e84841b8-6397-4b18-8a75-ee44592ab279)
![12](https://github.com/user-attachments/assets/fed20823-e904-4e4a-a092-c5faf7ff317b)

## URL

![13](https://github.com/user-attachments/assets/7bffb4b5-c18d-4624-8726-7e27df7a85fb)









