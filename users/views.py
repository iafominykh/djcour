from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from users.models import User


class IndexListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users'
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset()[:3]


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User
    template_name = 'users/users_detail.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    fields = ('full_name', 'email', 'image', 'comment')
    success_url = reverse_lazy('users:users_list')


class UserUpdateView(UpdateView):
    model = User
    fields = ('full_name', 'email', 'image', 'comment')
    success_url = reverse_lazy('users:index')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:users_list')
