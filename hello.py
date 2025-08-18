#!/usr/bin/env python3
"""Meu primeiro Hello world

Este codigo ele manda mensagem de Hello world de acordo com a linguem
que estiver configurada no ambiente da maquina, atraves de um modulo
padrao chamado OS.

explicando como fiz isso:
    criei uma variavel current_lenguage, importei um modulo padrao OS
    utilizei uma funcao do modulo os.getenv("LANG"), com essa funçao
    ele me retorna a lingua configurada no ENV.

    depois criei uma codiçao para colocar as linguas e a mensagem.
"""
__version__= "0.1.0"
__author__= "Pedro Henrique"
__license__= "unlicense"

import os

current_lenguage = os.getenv("LANG")[:5]

if current_lenguage == "pt_BR":
    msg = "Ola mundo!"
elif current_lenguage == "en_US":
    msg = "Hello world!"
elif current_lenguage == "es_ES":
    msg = "¡Hola, mundo!"
elif current_lenguage == "zh_CN":
    msg = "你好，世界"
elif current_lenguage == "ar_SA":
    msg = "مرحبا بالعالم"

print(msg)
