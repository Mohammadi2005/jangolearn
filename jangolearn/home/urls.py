from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.api, name='api'),
    path('show/', views.show, name='show'),
    path('detail/<slug:slug>', views.detail, name='detail'),
]