from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
    path('', views.main, name = 'main'),
    path('options/', views.options_menu, name = 'options_menu'),
    #path('login/', views.login, name= 'login'),
    #path('registration/', views.registration, name= 'registration'),
    path('settings/', views.settings, name= 'settings'),
    path('profile_update/', views.profile, name= 'profile'),
    path('creation_space/', views.creation, name= 'creation_space'),
    path('api/journal/create/', views.create_journal_entry, name='creation'),
]