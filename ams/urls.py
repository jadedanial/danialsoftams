from django.urls import path
from ams import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('<str:category>/view', views.ModuleView.as_view(), name='mod_view'),
    path('<str:category>/create/', views.ModuleCreate.as_view(), name='mod_create'),
    path('<str:category>/update/<int:pk>', views.ModuleUpdate.as_view(), name='mod_update'),
]