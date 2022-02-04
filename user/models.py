from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    # like one-to-many 임으로 따로 생성
    bio = models.TextField(max_length=500, blank=True)