from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Magazine(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class MyUser(AbstractUser):
    gender_choice = ((0, 'Nữ'), (1, 'Nam')) # 1 là giá trị thật sự, Nam là hiển thị ra bên ngoài
    age = models.IntegerField(default=0)
    gender = models.IntegerField(choices=gender_choice, default=0 )
    address = models.CharField(default='', max_length=255)
