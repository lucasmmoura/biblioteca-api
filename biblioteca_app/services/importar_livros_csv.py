import csv

from biblioteca_app.models.livros import Livro





def importar_livros(caminho_arquivo):
    """
    Importa livros a partir de um arquivo CSV.

    O arquivo deve conter as colunas:
    titulo, autor, categoria
    Cada lihna do arquivo, um novo livro é criado no bd
    
    """

    with open(caminho_arquivo, newline = "", encoding = "utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            Livro.objects.create(
                titulo = linha["titulo"],
                autor = linha["autor"],
                categoria = linha["categoria"]
            )