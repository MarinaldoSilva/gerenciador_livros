from django.urls import path
from .views import (
    UserCreateAPIView, UserReadAPIView, UserUpdateAPIView, UserDestroyAPIView
)

urlpatterns = [
    path("listar/", UserReadAPIView.as_view(), name="user-list"),
    path('registrar/', UserCreateAPIView.as_view(), name='user_register'),
    path('listar/<int:pk>/', UserReadAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
]