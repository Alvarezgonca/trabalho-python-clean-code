from datetime import date


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


class Emprestimo:
    def __init__(self, aluno, livro, data_emprestimo):
        self.aluno = aluno
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.devolvido = False

    def marcar_como_devolvido(self):
        self.devolvido = True

    def esta_ativo(self):
        return not self.devolvido


class Biblioteca:
    def __init__(self):
        self.emprestimos = []

    def registrar_emprestimo(self, aluno, livro):
        emprestimo = Emprestimo(aluno, livro, date.today())
        self.emprestimos.append(emprestimo)
        return emprestimo

    def listar_emprestimos_ativos(self):
        return [e for e in self.emprestimos if e.esta_ativo()]


if __name__ == "__main__":
    biblioteca = Biblioteca()
    aluno1 = Aluno("Carlos", "2023001")
    aluno2 = Aluno("Diana", "2023002")
    livro1 = Livro("Clean Code", "Robert C. Martin")
    livro2 = Livro("Refatoração", "Martin Fowler")

    emp1 = biblioteca.registrar_emprestimo(aluno1, livro1)
    biblioteca.registrar_emprestimo(aluno2, livro2)

    emp1.marcar_como_devolvido()

    print("Empréstimos ativos:")
    for emp in biblioteca.listar_emprestimos_ativos():
        print(f"- {emp.aluno.nome} pegou '{emp.livro.titulo}' em {emp.data_emprestimo}")
