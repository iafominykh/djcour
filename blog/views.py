from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    extra_context = {
        'title': 'Статьи'
    }

    def get_queryset(self):
        """Выводит список статей с положительным признаком публикации"""
        queryset = super().get_queryset()
        queryset = queryset.filter(is_publication=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data

    def get_object(self, **kwargs):
        views = super().get_object(**kwargs)
        views.count_views += 1
        views.save()
        return views


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')