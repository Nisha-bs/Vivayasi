from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.create_employee, name='create-employee'),
    path('farmer/', views.create_farmer, name='create-farmer'),
]