from django.urls import path
from .views import UserAPIView, UserListView, UserEditView, index, room

urlpatterns = [
    path('api/v1/user/', UserAPIView.as_view()),
    # path('<int:pk>/', UserView.as_view(), name='user_detail'),
    path('users', UserListView.as_view(), name='users'),
    path('<int:pk>/edit', UserEditView.as_view(), name='edit_user'),
    path('', index, name='chat'),
    path('<str:room_name>/', room, name='room'),   # путь для комнаты чата
]