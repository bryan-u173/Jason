from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('reto/<int:reto_id>/', views.detalle_reto, name='detalle_reto'),
]
