from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Recomendation, Category, State
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RecomendationForm, CategoryForm

# Create your views here.

#  State View
class StateDetailView(DetailView):
    model = State
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = State.objects.all()
        return context

# Category Views
class CategoryDetailView(DetailView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

@method_decorator(staff_member_required, name='dispatch')
class CategoryListView(ListView):
    model = Category
    paginate_by = 10

@method_decorator(staff_member_required, name='dispatch')
class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('recomend:list')

@method_decorator(staff_member_required, name='dispatch')
class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('recomend:list')

@method_decorator(staff_member_required, name='dispatch')
class CategoryDelete(DeleteView):
    model= Category
    success_url = reverse_lazy('recomend:list')

# Recomendations Views

class RecomendationListView(ListView):
    model = Recomendation
    paginate_by = 10

@method_decorator(staff_member_required, name='dispatch')
class RecomendationCreate(CreateView):
    model = Recomendation
    form_class = RecomendationForm
    success_url = reverse_lazy('recomend:list')

@method_decorator(staff_member_required, name='dispatch')
class RecomendationUpdate(UpdateView):
    model = Recomendation
    form_class = RecomendationForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('recomend:list')
    
@method_decorator(staff_member_required, name='dispatch')
class RecomendationDelete(DeleteView):
    model= Recomendation
    success_url = reverse_lazy('recomend:list')