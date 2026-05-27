class Produto:
    def __init__(self, nome, preco, categoria, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade_estoque = quantidade_estoque

    def valor_em_estoque(self):
        return self.preco * self.quantidade_estoque


class GerenciadorDeProdutos:
    def __init__(self):
        self.produtos = []

    def cadastrar(self, produto):
        self.produtos.append(produto)

    def listar(self):
        for produto in self.produtos:
            print(f"{produto.nome} | {produto.categoria} | "
                  f"R$ {produto.preco:.2f} | estoque: {produto.quantidade_estoque}")

    def calcular_valor_total_estoque(self):
        return sum(produto.valor_em_estoque() for produto in self.produtos)


if __name__ == "__main__":
    gerenciador = GerenciadorDeProdutos()
    gerenciador.cadastrar(Produto("Café", 25.00, "Bebidas", 50))
    gerenciador.cadastrar(Produto("Açúcar", 5.50, "Alimentos", 100))
    gerenciador.cadastrar(Produto("Caneca", 18.00, "Utensílios", 30))

    gerenciador.listar()
    print(f"\nValor total em estoque: R$ {gerenciador.calcular_valor_total_estoque():.2f}")
