from django.urls import path
from rest_framework import routers
#ViewSet에 딸린 라우터 기능을 쓰기 위함
from .views import PostViewSet, CommentViewSet, like_post


router = routers.SimpleRouter() #심플라우터 하나를 생성
router.register('posts', PostViewSet) #라우터에 posts를 등록하고 PostViewSet의 정보를 쓴다.
router.register('comments', CommentViewSet)

#url패턴은 라우터의 정보를 기반으로한다.
urlpatterns = router.urls + [
        path('like/<int:pk>/', like_post, name='like_post')
]
