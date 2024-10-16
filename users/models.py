from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField('Avatar', upload_to='profile_avatar', null=True, blank=True)
    role = models.CharField('Role', default='user', max_length=20)
    # is_blocked = models.BooleanField('Is blocked', default=False)
    is_active = True

    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.id}- {self.username}'


