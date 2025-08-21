#!/usr/bin/env python3
"""Exibe relatorio de atividades
"""
__version__ = "0.2.0"
__author__ = "Pedro Henrique"
__license__ = "unlicense"

#Dados
salas = {
    "sala 1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala 2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

atividades = {
    "ingles":["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "musica":["Erik", "Carlos", "Maria"],
    "natacao":["Gustavo", "Sofia", "Joana", "Antonio"],
}

for atividade, aluno_atividade  in atividades.items():
    print(f"\n {atividade.upper()}")
    for sala, alunos_sala in salas.items():
        participantes = set(alunos_sala) & set(aluno_atividade)   
        print(f"{sala}: {participantes}")
