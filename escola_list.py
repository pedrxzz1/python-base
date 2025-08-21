#!/usr/bin/env python3
"""Exibe relatorio de atividades
"""
__version__ = "0.0.1"
__author__ = "Pedro Henrique"
__license__ = "unlicense"

#Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_natacao = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("ingles", aula_ingles),
    ("musica", aula_musica),
    ("natacao", aula_natacao),
]

for nome_atividade, atividade in atividades:

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
            
    print(f"{nome_atividade} sala 1: ", atividade_sala1)
    print(f"{nome_atividade} sala 2: ", atividade_sala2)
    print()
    print("#"*40)
    print()
