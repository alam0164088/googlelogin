from django.contrib import admin
from django.urls import path, include
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
]