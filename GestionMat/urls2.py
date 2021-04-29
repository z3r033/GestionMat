from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
 # material views


path('ds', views.dashboard, name='dashboard'),
path('enregistrer/', views.enregistrer, name='enregistrer'),
 path('login/', auth_views.LoginView.as_view(), name='login'),
 path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# change password urls
path('password_change/',
 auth_views.PasswordChangeView.as_view(),
 name='password_change'),
path('password_change/done/',
 auth_views.PasswordChangeDoneView.as_view(),
 name='password_change_done'),

path('edit/', views.edituser, name='edit'),

]