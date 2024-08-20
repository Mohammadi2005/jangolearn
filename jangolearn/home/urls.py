from django.urls import path
from . import views  # همه توابع views رو فراخوانی میکنه

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.api, name='api'),
    path('show/', views.show, name='show'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('category/<slug:slug>', views.category, name='category'),
]