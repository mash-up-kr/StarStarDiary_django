from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom UserModel 정
    """
    nickname = models.CharField('닉네임', max_length=50, blank=True)
    img_profile = models.ImageField('프로필 이미지', blank=True)
