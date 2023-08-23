import django
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog
from main.forms import CustomerForm, MessageForm
from main.models import Customer, Message, Mailing, Attempt
from main.services import send_email


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailing_count'] = Mailing.objects.all().count()
        context_data['active_mailing_count'] = Mailing.objects.filter(status=Mailing.CREATED).count()
        context_data['count_unique_clients'] = Customer.objects.filter(is_active=True).count()
        context_data['blog_list'] = Blog.objects.all().order_by('?')[:3]
        return context_data


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    extra_context = {
        'title': 'Клиенты'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('main.view_customer'):
            return queryset
        return Customer.objects.filter(created_by=self.request.user)


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('main:customer_list')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('main:customer_list')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('main:customer_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'title': 'Сообщения'
    }


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('main:message_list')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    extra_context = {
        'title': 'Рассылки'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('main.view_mailing'):
            return queryset

        return queryset.filter(created_by=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    fields = ('mailing_time', 'message', 'frequency', 'status', 'created_by')
    success_url = reverse_lazy('main:mailing_list')
    try:
        for send in Mailing.objects.all():
            if send.status == Mailing.CREATED:
                send_email(Mailing.ONCE)
    except django.db.utils.ProgrammingError:
        print('ProgrammingError')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ('message', 'frequency', 'status',)
    success_url = reverse_lazy('main:mailing_list')


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:mailing_list')


class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    extra_context = {
        'title': 'Статистика'
    }


class AttemptDetailView(LoginRequiredMixin, DetailView):
    model = Attempt

@permission_required(perm='main.set_mailing_status')
def set_mailing_status(request, pk):
    """Отключение рассылки"""
    mailing_item = get_object_or_404(Mailing, pk=pk)
    if mailing_item.status == Mailing.CREATED:
        mailing_item.status = Mailing.COMPLETED
        mailing_item.save()
    else:
        mailing_item.status = Mailing.CREATED
        mailing_item.save()
    return redirect(reverse('main:mailing_list'))


@permission_required(perm='main.set_is_active')
def set_is_active(request, pk):
    "Статус пользователя"
    customer_item = get_object_or_404(Customer, pk=pk)
    if customer_item.is_active:
        customer_item.is_active = False
    else:
        customer_item.is_active = True
    customer_item.save()
    return redirect(reverse('main:customer_list'))
