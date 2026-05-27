# Lista de Exercícios — Clean Code e SOLID com Python

Disciplina: Arquitetura e Projeto de Software.

Repositório com 15 exercícios sobre Clean Code e os princípios SOLID, cada um em um arquivo `.py` independente e executável.

## Como executar

Requer Python 3.8 ou superior.

```bash
python3 exercicio_01.py
python3 exercicio_02.py
# ...
python3 exercicio_15.py
```

Para rodar todos de uma vez:

```bash
for f in exercicio_*.py; do echo "=== $f ==="; python3 "$f"; done
```

## Exercícios

| Arquivo | Tema |
|---|---|
| `exercicio_01.py` | Nomes significativos |
| `exercicio_02.py` | Removendo código duplicado |
| `exercicio_03.py` | Função com responsabilidade única |
| `exercicio_04.py` | Evitando números mágicos |
| `exercicio_05.py` | Agrupando atributos em uma classe |
| `exercicio_06.py` | SRP em sistema de relatório |
| `exercicio_07.py` | OCP no cálculo de desconto |
| `exercicio_08.py` | LSP em formas geométricas |
| `exercicio_09.py` | Evitando violação do LSP (aves) |
| `exercicio_10.py` | ISP em dispositivos eletrônicos |
| `exercicio_11.py` | DIP em envio de notificações |
| `exercicio_12.py` | Cadastro de produtos |
| `exercicio_13.py` | Sistema de biblioteca |
| `exercicio_14.py` | Sistema de pagamento (OCP + DIP) |
| `exercicio_15.py` | Mini projeto: sistema de pedidos aplicando Clean Code e SOLID |

## Princípios SOLID aplicados

- **SRP** (Single Responsibility) — exercícios 3, 6, 12, 13, 15
- **OCP** (Open/Closed) — exercícios 7, 14, 15
- **LSP** (Liskov Substitution) — exercícios 8, 9, 15
- **ISP** (Interface Segregation) — exercícios 10, 15
- **DIP** (Dependency Inversion) — exercícios 11, 14, 15

## Estrutura do projeto

```
.
├── exercicio_01.py ... exercicio_15.py
├── README.md
└── .gitignore
```
