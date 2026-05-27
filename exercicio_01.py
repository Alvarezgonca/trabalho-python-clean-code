def calcular_valor_total_compra(quantidade_itens, preco_unitario):
    return quantidade_itens * preco_unitario


if __name__ == "__main__":
    total = calcular_valor_total_compra(3, 49.90)
    print(f"Valor total da compra: R$ {total:.2f}")
