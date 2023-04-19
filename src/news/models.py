from django.db import models
from django.utils import timezone

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=255, blank=False, null=False) # bank=False không được rỗng, null=False (không được null)
#     content = models.TextField(max_length=1000, blank=False, null=False)
#     time_create = models.DateTimeField(default=timezone.datetime.now())
#     # django.utils.timezone.now

#     def __str__(self): # cấu hình trong /admin
#         return self.title # hiển thị title ra thay vì Object