from django.urls import path
from biblioteca_app.views.emprestimos import EmprestimoListCreateView, EmprestimoAtivoView, EmprestimoAtrasadoView, HistoricoUsuarioView
from biblioteca_app.views.usuarios import UsuarioListCreateView
from biblioteca_app.views.livros import LivroListCreateView, LivroDisponivelView

urlpatterns = [

    path("emprestimos/", EmprestimoListCreateView.as_view()),
    path("emprestimos/ativos/", EmprestimoAtivoView.as_view()),
    path("emprestimos/atrasados/", EmprestimoAtrasadoView.as_view()),

    path("usuarios/", UsuarioListCreateView.as_view()),
    path("usuarios/<int:usuario_id>/historico/", HistoricoUsuarioView.as_view()),

    path("livros/", LivroListCreateView.as_view()),
    path("livros/disponiveis/", LivroDisponivelView.as_view()),

]