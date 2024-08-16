from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from users.models import Profile

# Create your models here.

# 글쓰기 기능
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    #Foreign Key로 씀(User측에서 지워지면 같이 지워짐)
    #Primary Key 는 자동으로 생성
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True) #없으면 그냥 비워둔다.
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField() #본문
    image = models.ImageField(upload_to='post/', default='default.png') #저장은 post에, 디폴트값
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)
    published_date = models.DateTimeField(default=timezone.now)
