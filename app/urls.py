from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio,name='index'),
    path('placa/',placa,name='placa'),
    path('registro/',registro,name='registro'),
    path('sol_informe/',sol_informe,name='sol_informe'),
    path('usuario/',usuariopag,name='usuario'),
    path('lista-solicitud/',lista_view,name='lista'),
    path('solicitudes/', solicitud_list, name='solicitud-list'),
    ]