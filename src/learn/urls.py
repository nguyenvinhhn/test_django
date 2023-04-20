from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path('', views.ListCreateCarView.as_view()),
    # path(r'api/data/', getJson, name='getJson'),
    # path('cars/<int:pk>', views.UpdateDeleteCarView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('info/', views.TestAPIView.as_view(), name='info'),
    path('check-no-auth/', views.NotAuthenAPIView.as_view(), name='check_no_auth'),
]
