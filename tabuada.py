#!/usr/bin/env python3
"""Tabuada simples
"""
__version__ = "0.0.1"
__author__ = "Pedro Henrique"
__license__ = "unlicense"

numeros = list(range(1,11))

for n1 in numeros:
    print("Tabuada do numero:", n1)
    for n2 in numeros:
        print(n1*n2)
    print(25*"-")
