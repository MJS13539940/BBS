from django.urls import path
from .views import RegisterView, LoginView, ProfileView

#레지스터API의 경로
urlpatterns = [
    path('register/', RegisterView.as_view()), #클래스를 뷰로 인식해서 쓰기위해 as_view를 쓴다.
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()), #프로필 주인에대한 개별 주소를 할당
]
