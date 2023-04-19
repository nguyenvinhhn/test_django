from django.contrib import admin

# Register your models here.
from . models import Magazine, MyUser

admin.site.register(Magazine)
admin.site.register(MyUser)

