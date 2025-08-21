#!/usr/bin/env python3
"""cadastro de produtos
"""
__version__ = "0.0.1"
__author__ = "Pedro Henrique"
__license__ = "unlicense"

from pprint import pprint

produto = {
    "nome": "caneta",
    "cores": ["azul", "vermelha", "preta"],
    "preco": 1.99,
    "dimensao": {
        "altura": 12,
        "largura": 0.8,
    },
    "estoque": True,
}

cliente = {
    "nome": "Bruno",
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 5,
}

total_compra = compra["quantidade"] * produto["preco"]

print(
    f" O {compra["cliente"]["nome"]} comprou {compra["quantidade"]}"
    f" unidades de {produto["nome"]},"
    f" total da compra ficou {total_compra}"
)
