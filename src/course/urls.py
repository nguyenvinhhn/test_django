from django.urls import path
from . import views
from .views import GetAllCourseAPIView

urlpatterns = [
    path(r'courses', GetAllCourseAPIView.as_view(), name='courses'),
]