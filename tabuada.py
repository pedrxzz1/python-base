#!/usr/bin/env python3
"""Tabuada simples
Primeira versao simples

Proximo passo: 
    adicionarei o .format para centralizar os numeros e deixar
    o programa agradavel visualmente.

"""
__version__ = "0.0.1"
__author__ = "Pedro Henrique"
__license__ = "unlicense"

numeros = list(range(1,11))

for n1 in numeros:
    print("{:-^20}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        res = n1*n2
        print("{:^20}".format(f"{n1} x {n2} = {res}"))
    print()
    print("#"*20)
