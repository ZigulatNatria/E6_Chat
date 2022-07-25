from django.shortcuts import render
from rest_framework import generics
from .models import Message, Room, User
from .serializers import UserSerializer
from django.views.generic import DetailView, ListView, UpdateView
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


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer