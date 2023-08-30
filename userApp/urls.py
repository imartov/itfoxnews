from django.urls import path
from .views import AdminRegistrationView


urlpatterns = [
    # http://127.0.0.1:8000/api/basicauth/admin/register/
    path('admin/register/', AdminRegistrationView.as_view(), name='admin_register'),
]
