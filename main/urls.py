from django.urls import path, include
from . import views
from django.conf import settings
from django.urls import path
from .views import create_journal_entry

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
    path('api/journal/create/', create_journal_entry, name='create_journal'),
    path('journal/edit/<int:entry_id>/', views.edit_journal_entry, name='edit_journal'),
    path('journal/delete/<int:entry_id>/', views.delete_journal_entry, name='delete_journal'),
    path('journal/edit-page/<int:entry_id>/', views.edit_journal_page, name='edit_journal_page'),
    #path('profile/upload-picture/', views.update_profile_picture, name='upload_profile_pic'),
    
]