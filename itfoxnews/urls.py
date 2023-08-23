"""
URL configuration for itfoxnews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('newsApp.urls')),

    # base auth
    path('api/baseauth/', include('rest_framework.urls')),
    # http://127.0.0.1:8000/api/baseauth/login/ - base log in
    
    path('api/djoserauth/', include('djoser.urls')),
    # http://127.0.0.1:8000/api/djoserauth/
    # http://127.0.0.1:8000/api/djoserauth/users/ - create new user 
    # http://127.0.0.1:8000/api/djoserauth/users/activation/ - activation user
    # more - https://djoser.readthedocs.io/en/latest/base_endpoints.html#user-create

    # token auth
    re_path(r'^api/auth/', include('djoser.urls.authtoken')),
    # http://127.0.0.1:8000/api/auth/token/login/ - get token

    # Json Web Token auth
    path('api/jwtoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # http://127.0.0.1:8000/api/jwttoken/
    path('api/jwtoken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/jwtoken/verify/', TokenVerifyView.as_view(), name='token_verify')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)