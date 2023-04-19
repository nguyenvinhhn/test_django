"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


# from myapp.views import ShowHelloWorld, index_view, IndexView, tester, viewlist

from user import views as UserViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('core.urls')),
    # url(r'^$', UserViews.indexHome),
    # path('home/', index_view, name='home'),
    # path("myapp/", include("myapp.urls")),
    # path('demo/', IndexView.as_view(), name='abc' ),
    # path('demo-new/', IndexView.as_view(), name='abc' ),
    # path('demo-new-2/', IndexView.as_view(), name='abc' ),
    # path('demo-new-4/', IndexView.as_view(), name='abc' ),
    # path('demo-new-5/', IndexView.as_view(), name='abc' ),
    # path("news/", include("news.urls")),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
