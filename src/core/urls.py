from django.urls import path
from . import views

app_name = 'Login'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view' ),
    # path('login/', views.LoginClass.as_view(), name='login' ),
    # path('user-view/', views.ViewUser.as_view(), name='user_view' ),
    # path('view-pro/', views.view_product , name='view_pro' ),
    # path('add-manazine/', views.AddManazineClass.as_view() , name='add_manazine' ),
]


