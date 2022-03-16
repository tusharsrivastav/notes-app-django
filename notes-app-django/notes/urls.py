from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('add/', views.add, name='add'),
    path('delete/<int:note_id>', views.delete, name='delete'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('note/<int:id>/edit/', views.detail_edit, name='detail_edit'),
]
