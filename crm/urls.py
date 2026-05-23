from django.urls import path
from . import views

urlpatterns = [
    # Rutas de Clientes
    path('clientes/', views.ClientListView.as_view(), name='client_list'),
    path('clientes/nuevo/', views.ClientCreateView.as_view(), name='client_create'),
    path('clientes/<int:pk>/editar/', views.ClientUpdateView.as_view(), name='client_update'),
    path('clientes/<int:pk>/eliminar/', views.ClientDeleteView.as_view(), name='client_delete'),
    
    # Rutas de Interacciones
    path('interacciones/', views.InteractionListView.as_view(), name='interaction_list'),
    path('interacciones/nueva/', views.InteractionCreateView.as_view(), name='interaction_create'),
    path('interacciones/<int:pk>/editar/', views.InteractionUpdateView.as_view(), name='interaction_update'),
    path('interacciones/<int:pk>/eliminar/', views.InteractionDeleteView.as_view(), name='interaction_delete'),
]