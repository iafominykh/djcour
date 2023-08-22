from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from main.apps import MainConfig
from main.views import IndexView, CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, \
    CustomerDeleteView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, AttemptListView, AttemptDetailView, \
    set_mailing_status, MailingDeleteView, set_is_active

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(IndexView.as_view()), name='Index'),
    path('customers/', never_cache(CustomerListView.as_view()), name='customer_list'),
    path('customer_detail/<int:pk>/', cache_page(60)(CustomerDetailView.as_view()), name='customer_detail'),
    path('customers/create/', cache_page(60)(CustomerCreateView.as_view()), name='customer_create'),
    path('customers/update/<int:pk>', cache_page(60)(CustomerUpdateView.as_view()), name='customer_update'),
    path('customers/delete/<int:pk>', cache_page(60)(CustomerDeleteView.as_view()), name='customer_delete'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('message_detail/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('messages/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('attempt/', AttemptListView.as_view(), name='attempt_list'),
    path('attempt/<int:pk>/', AttemptDetailView.as_view(), name='attempt_detail'),
    path('set_mailing_status/<int:pk>', login_required(set_mailing_status), name='set_mailing_status'),
    path('set_is_active/<int:pk>', login_required(set_is_active), name='set_is_active'),

]