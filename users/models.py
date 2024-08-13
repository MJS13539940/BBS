from django.db import models
from django.contrib.auth.models import User # 유저와 프로필을 1:1로 대응시키기 위해선 정보가 있어야함
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#프로필
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    #1:1 대응용 필드, 삭제가 될 경우 둘 다 같이 삭제되도록 한다.
    nickname = models.CharField(max_length=128)
    position = models.CharField(max_length=128) #직종
    subject = models.CharField(max_length=128) #관심사
    image = models.ImageField(upload_to='profile/', default='default.png') 
    #profile 이란 경로에 업로드하고 디폴트는 png로한다.

#데코레이터를 통해 데이터를 전달받음
#자동으로 데이터를 받게 해준다.
@receiver(post_save, sender=User) #유저로부터 받은 post_save의 내용을 아래의 함수에 전달
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
