from django.contrib import admin
from .models import Course

# Register your models here.

# @admin.register(Course)
# class Courses(admin.ModelAdmin):
#     list_display=['id', 'title', 'content']
#     # list_display=['id','price', 'title', 'content']
#     admin.register(Course)

admin.site.register(Course)