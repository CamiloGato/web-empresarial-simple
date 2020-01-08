from django.contrib import admin
from django.urls import path, include
from .views import RecomendationListView, RecomendationCreate, RecomendationDelete, RecomendationListView, RecomendationUpdate
from .views import CategoryCreate, CategoryDelete, CategoryDetailView, CategoryUpdate, CategoryListView
from .views import StateDetailView

recomend_patterns = ([
    path('', RecomendationListView.as_view(), name='list'),
    path('create/', RecomendationCreate.as_view(), name='create'),
    path('update/<int:pk>/', RecomendationUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', RecomendationDelete.as_view(), name='delete'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/<slug:name>/', CategoryDetailView.as_view(), name='category'),
    path('category_create/', CategoryCreate.as_view(), name='category_create'),
    path('category_update/<int:pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', CategoryDelete.as_view(), name='category_delete'),
    path('state/<int:pk>/<slug:name>', StateDetailView.as_view(), name='state'),
], 'recomend')