from django.urls import path
from . import views
from .viewset import getJson

urlpatterns = [
    path('cars', views.ListCreateCarView.as_view()),
    path(r'api/data/', getJson, name='getJson'),
    path('cars/<int:pk>', views.UpdateDeleteCarView.as_view()),
]