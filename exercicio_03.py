LIMITE_DESCONTO = 100
TAXA_DESCONTO = 0.10


def calcular_desconto(valor):
    if valor > LIMITE_DESCONTO:
        return valor * TAXA_DESCONTO
    return 0


def calcular_valor_final(valor, desconto):
    return valor - desconto


def exibir_dados_pedido(nome_cliente, valor, valor_final):
    print(f"Cliente: {nome_cliente}")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")


def processar_pedido(nome_cliente, valor):
    desconto = calcular_desconto(valor)
    valor_final = calcular_valor_final(valor, desconto)
    exibir_dados_pedido(nome_cliente, valor, valor_final)


if __name__ == "__main__":
    processar_pedido("Maria", 250)
    processar_pedido("João", 80)
