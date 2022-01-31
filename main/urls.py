from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('updates', views.updates, name='updates'),
]