#!/usr/bin/env python3
"""Calculadora prefix

funcionamento:

[operaçao] [n1] [n2]

operacoes:
sum-> +
sub-> -
mul->
div->

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

"""
__version__ = "0.1.0"
__author__ = "Pedro Henrique"
__license__ = "unlicense"

import sys

arguments = sys.argv[1:]

operation, *nums = arguments

validated_nums = []

for num in nums:
    validated_nums.append(int(num))

n1, n2 = validated_nums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"You result is {result}! \N{party popper}")
