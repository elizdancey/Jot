from django.urls import path
from . import views

urlpatterns = [
    path('jot/', views.main, name = 'main'),
]