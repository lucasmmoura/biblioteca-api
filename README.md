# Sistema de Gerenciamento de Biblioteca

## Descrição

API desenvolvida em Django Rest Framework para gerenciamento de empréstimos de livros em uma biblioteca.

## Funcionalidades

- Cadastro de livros
- Cadastro de usuários
- Cadastro de empréstimos
- Autenticação por Token
- Controle de disponibilidade dos livros
- Histórico de empréstimos por usuário
- Consulta de empréstimos ativos
- Consulta de empréstimos atrasados
- Relatório de livros mais emprestados
- Relatório de empréstimos por período
- Filtro de livros por categoria
- Importação de livros via CSV
- Cálculo automático de multas
- Renovação de empréstimos
- Devolução automática de livros

## Tecnologias

- Python
- Django
- Django Rest Framework
- MySQL
- Git
- GitHub

## Regras de Negócio

### Empréstimos

- Livros indisponíveis não podem ser emprestados.
- A data prevista de devolução é gerada automaticamente com prazo de 7 dias.
- O empréstimo é criado como ativo automaticamente.

### Renovação

- Cada renovação adiciona 7 dias ao prazo.
- O limite máximo é de 5 renovações.
- Apenas empréstimos ativos podem ser renovados.
- A renovação só pode ocorrer na data prevista de devolução ou após ela.

### Devolução

- A devolução encerra automaticamente o empréstimo.
- O livro volta a ficar disponível.

### Multa

- Multa de R$ 2,00 por dia de atraso.

## Testes

Foram implementados testes automatizados para validar:

- Geração automática da data de devolução
- Bloqueio de empréstimos para livros indisponíveis
- Limite de renovações
- Cálculo automático de multas



## Endpoints

### Livros

| Método | Endpoint | Descrição |
|----------|----------|----------|
| GET | /api/livros/ | Lista livros |
| POST | /api/livros/ | Cadastra livro |
| GET | /api/livros/disponiveis/ | Lista livros disponíveis |
| GET | /api/livros/mais-emprestados/ | Relatório de livros mais emprestados |
| GET | /api/livros/categoria/?categoria=Fantasia | Filtra livros por categoria |

### Usuários

| Método | Endpoint | Descrição |
|----------|----------|----------|
| GET | /api/usuarios/ | Lista usuários |
| POST | /api/usuarios/ | Cadastra usuário |
| GET | /api/usuarios/<id>/historico/ | Histórico de empréstimos |

### Empréstimos

| Método | Endpoint | Descrição |
|----------|----------|----------|
| GET | /api/emprestimos/ | Lista empréstimos |
| POST | /api/emprestimos/ | Cria empréstimo |
| GET | /api/emprestimos/ativos/ | Lista empréstimos ativos |
| GET | /api/emprestimos/atrasados/ | Lista empréstimos atrasados |
| GET | /api/emprestimos/periodo/?inicio=AAAA-MM-DD&fim=AAAA-MM-DD | Relatório por período |