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
    path('', views.index, name='index' ),
    path('add/', views.add_post, name='add' ),
    path('save/', views.save_news, name='save' ),
    path('email/', views.email_view, name='email' ),
    path('process/', views.process, name='process' ),

]

