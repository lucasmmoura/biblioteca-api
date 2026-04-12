from django.urls import path
from biblioteca_app.views.emprestimos import EmprestimoListCreateView
from biblioteca_app.views.usuarios import UsuarioListCreateView
from biblioteca_app.views.livros import LivroListCreateView

urlpatterns = [

    path("emprestimos/", EmprestimoListCreateView.as_view()),
    path("usuarios/", UsuarioListCreateView.as_view()),
    path("livros/", LivroListCreateView.as_view())

]