from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='custom-token'),
]