from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservationproduct/<int:id>/', views.reservationproduct, name='reservationproduct')
]
