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

if not arguments:
    operation = input("Operation:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif arguments !=3:
    print("Invalid Operation")
    print("Ex: `sum 5 5`")
    sys.exit(1)
    
operation, *nums = arguments

validated_operation = ("sum", "sub", "mul", "div")
if operation not in validated_operation:
    print("Invalid Operation!")
    print(validated_operation)
    sys.exit(1)

    
validated_nums = []
for num in nums:
    if (".") in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"Your result is: {result} \N{party popper}\N{party popper}!")
