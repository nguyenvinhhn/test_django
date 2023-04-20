from rest_framework import serializers
from .models import Course

class GetAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', )

class CourseSerializer(serializers.Serializer): # serializers cơ bản, nâng cao làm giống GetAllCourseSerializer
    title1 = serializers.CharField(max_length=32)
    content1 = serializers.CharField(max_length=32)
    price1 = serializers.IntegerField()