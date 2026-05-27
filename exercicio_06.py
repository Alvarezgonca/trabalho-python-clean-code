class GeradorDeDados:
    def gerar(self):
        return ["Produto A", "Produto B", "Produto C"]


class FormatadorDeRelatorio:
    def formatar(self, dados):
        return "\n".join(dados)


class SalvadorDeArquivo:
    def salvar(self, conteudo, caminho):
        with open(caminho, "w") as arquivo:
            arquivo.write(conteudo)


if __name__ == "__main__":
    dados = GeradorDeDados().gerar()
    conteudo = FormatadorDeRelatorio().formatar(dados)
    SalvadorDeArquivo().salvar(conteudo, "relatorio.txt")
    print("Relatório gerado com sucesso.")
