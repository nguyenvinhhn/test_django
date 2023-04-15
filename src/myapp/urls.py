
from django.urls import path
from . import views
from myapp.views import ShowHelloWorld, index_view, IndexView, tester

urlpatterns = [
    path('index_view/', views.index_view, name='index_view'),
    path('tester/', tester ),
]
