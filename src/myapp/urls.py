
from django.urls import path
from . import views
from myapp.views import ShowHelloWorld, index_view, IndexView, tester, viewlist, detailView
from myapp import views 

app_name = 'myapp'
urlpatterns = [
    path('index_view/', views.index_view, name='index_view'),
    path('index_view-2/', views.index_view, name='index_view'),
    path('tester/', tester ),
    path('list/', viewlist, name='view_list' ),
    path('detail/<int:question_id>', views.detailView, name='detail' ),
    path('<int:question_id>', views.vote, name='vote' ),
]
