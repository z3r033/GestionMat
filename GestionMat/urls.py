from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'GestionMat' #namespace
urlpatterns = [
 # material views

 path('', views.materials_list, name='materials_list'),

 #path('<int:year>/<int:month>/<int:day>/<str:numero_serie>/',
 path('<int:year>/<str:numero_serie>/',
 views.material_detail,
 name='material_detail'),
 path('add/', views.addmaterial, name='add'),
 path('<str:num_serie>/delete/', views.removematerial, name='delete'),
 path('<str:num_serie>/update/', views.updatemat, name='update'),
path('search/', views.mat_search, name='mat_search'),
path('gsearch/', views.garrenti_search, name='garrenti_search'),
#path('ds', views.dashboard, name='dashboard'),
#path('update/', views.updatemat, name='update'),


]