class Cliente:
    def __init__(self, nome, email, telefone, cpf):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf


def exibir_dados_cliente(cliente):
    print("=== Dados do Cliente ===")
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")
    print(f"CPF: {cliente.cpf}")
    print()


if __name__ == "__main__":
    cliente1 = Cliente("Ana Silva", "ana@email.com", "21999990000", "111.222.333-44")
    cliente2 = Cliente("Bruno Souza", "bruno@email.com", "21988887777", "555.666.777-88")
    exibir_dados_cliente(cliente1)
    exibir_dados_cliente(cliente2)
