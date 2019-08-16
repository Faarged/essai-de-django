from django.urls import path

from . import views

urlpatterns = [
    path('date', views.date_actuelle),
    path('', views.index, name='index'),
]
