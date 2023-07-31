from django.urls import path

from users.apps import UsersConfig
from users.views import UserListView, UserDetailView, UserCreateView, IndexListView, UserUpdateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='users_detail'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='users_confirm_delete'),

]