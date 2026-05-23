from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client, Interaction
from .forms import ClientForm, InteractionForm

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(email__icontains=query) |
                Q(company__name__icontains=query)
            )
        return queryset

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        form.instance.commercial = self.request.user 
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

class InteractionListView(LoginRequiredMixin, ListView):
    model = Interaction
    template_name = 'interaction_list.html'
    context_object_name = 'interactions'

class InteractionCreateView(LoginRequiredMixin, CreateView):
    model = Interaction
    form_class = InteractionForm
    template_name = 'interaction_form.html'
    success_url = reverse_lazy('interaction_list')

class InteractionUpdateView(LoginRequiredMixin, UpdateView):
    model = Interaction
    form_class = InteractionForm
    template_name = 'interaction_form.html'
    success_url = reverse_lazy('interaction_list')

class InteractionDeleteView(LoginRequiredMixin, DeleteView):
    model = Interaction
    template_name = 'interaction_confirm_delete.html'
    success_url = reverse_lazy('interaction_list')