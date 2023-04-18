from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    # path('index_view/', views.index_view, name='index_view'),
    # path('index_view-2/', views.index_view, name='index_view'),
    # path('tester/', tester ),
    # path('list/', viewlist, name='view_list' ),
    # path('detail/<int:question_id>', views.detailView, name='detail' ),
    # path('<int:question_id>', views.vote, name='vote' ),
    path('', views.IndexClass.as_view(), name='index' ),
    path('save/', views.ClassSaveNews.as_view(), name='save' ),
    path('email/', views.email_view, name='email' ),
    path('process/', views.process, name='process' ),

]

