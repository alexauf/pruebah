from django.contrib import admin
from django.urls import path
from pruebahApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tienda/', views.tienda, name='tienda'),
]
