from django.shortcuts import render, redirect, reverse
from rest_framework import viewsets
from .models import Message, Room, User
from .serializers import UserSerializer, RoomSerializer, MessageSerializer
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserEditForm

# class UserView(DetailView):
#     model = User
#     context_object_name = 'user'
#     template_name = 'user.html'
#     queryset = User.objects.all()

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'user.html'
    queryset = User.objects.all()


class UserEditView(UpdateView):
    model = User
    template_name = 'edit_user.html'
    form_class = UserEditForm
    success_url = '/'


def index(request):
    return render(request, 'chat.html') #главная страница

# функция-представление для комнаты чата
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })


class MessageListView(ListView):
    model = User
    context_object_name = 'messages'
    template_name = 'messages.html'
    queryset = Message.objects.all()


class RoomDetail(DetailView):
    model = Room
    template_name = 'room_detail.html'
    context_object_name = 'roomm'
    queryset = Room.objects.all()


class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class RoomAPIView(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('name')
    serializer_class = RoomSerializer


class MessageAPIView(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('message')
    serializer_class = MessageSerializer