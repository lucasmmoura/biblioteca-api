from django.contrib import admin
from .models import Livro, Usuario, Emprestimo
from datetime import date
from django.core.exceptions import ValidationError



admin.site.register(Livro)
admin.site.register(Usuario)


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):

    actions = [
        "devolver_livro",
        "renovar_emprestimo"
    ]

    list_display = (
        "usuario",
        "livro",
        "ativo",
        "data_prevista_devolucao"
    )

    readonly_fields = (
        "data_prevista_devolucao",
        "valor_multa",
        "quantidade_renovacoes",
        "data_devolucao",
        "ativo",
    )

    exclude = (
        "ativo",
    )


    def devolver_livro(self, request, queryset):

        for emprestimos in queryset:
            emprestimos.data_devolucao = date.today()
            emprestimos.save()

    devolver_livro.short_description = "Devolver livro"




    def renovar_emprestimo(self, request, queryset):

        for emprestimo in queryset:
            try:
                emprestimo.renovar()

            except ValidationError as erro:
                self.message_user(
                    request,
                    erro.message,
                    level = "ERROR"
                )

    renovar_emprestimo.shot_description = (
        "Renovar empréstimo"
    )
