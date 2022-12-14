from django.contrib import admin
from django.urls import path, include
from ams import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ams/', include('ams.urls')),
]