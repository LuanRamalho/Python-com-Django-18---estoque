from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('nota/nova/', views.adicionar_nota, name='adicionar_nota'),
    path('nota/editar/<int:id>/', views.editar_nota, name='editar_nota'),
    path('nota/excluir/<int:id>/', views.excluir_nota, name='excluir_nota'),
    path('nota/<int:nota_id>/', views.lista_produtos, name='lista_produtos'),

    path('produto/novo/<int:nota_id>/', views.adicionar_produto, name='adicionar_produto'),
    path('produto/editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('produto/excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
]
