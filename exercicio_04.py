VALOR_MINIMO_FRETE_GRATIS = 200
VALOR_PADRAO_FRETE = 25


def calcular_frete(valor_compra):
    if valor_compra >= VALOR_MINIMO_FRETE_GRATIS:
        return 0
    return VALOR_PADRAO_FRETE


if __name__ == "__main__":
    print(f"Frete (R$150): R$ {calcular_frete(150)}")
    print(f"Frete (R$250): R$ {calcular_frete(250)}")
