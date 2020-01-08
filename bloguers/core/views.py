from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'core/index.html'

class BlogTemplateView(TemplateView):
    template_name = 'core/blog.html'