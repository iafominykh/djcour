from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from distribution.models import Distribution


# Create your views here.
class DistributionListView(ListView):
    model = Distribution


class DistributionDetailView(DetailView):
    model = Distribution
    template_name = 'distribution/distribution_detail.html'
    context_object_name = 'distribution'


class DistributionCreateView(CreateView):
    model = Distribution
    fields = ('start_time', 'end_time', 'frequency', 'status')
    success_url = reverse_lazy('distribution:distribution_list')


class DistributionUpdateView(UpdateView):
    model = Distribution
    fields = ('start_time', 'end_time', 'frequency', 'status')
    success_url = reverse_lazy('distribution:distribution_list')


class DistributionDeleteView(DeleteView):
    model = Distribution
    fields = ('start_time', 'end_time', 'frequency', 'status')
    success_url = reverse_lazy('distribution:distribution_list')
