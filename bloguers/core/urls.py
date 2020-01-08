from django.contrib import admin
from django.urls import path, include
from .views import HomeTemplateView, BlogTemplateView

home_patterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('blog/', BlogTemplateView.as_view(), name='blog'),
    path('admin/', admin.site.urls),
]