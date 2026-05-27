def calcular_preco_com_desconto(preco, taxa_desconto):
    desconto = preco * taxa_desconto
    return preco - desconto


if __name__ == "__main__":
    taxa = 0.10
    precos = [100, 250, 80]
    for preco in precos:
        print(f"Preço final: R$ {calcular_preco_com_desconto(preco, taxa):.2f}")
