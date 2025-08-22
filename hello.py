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

execuçao:
    python3 hello.py
    ou
    ./hello.py
"""
__version__= "0.1.3"
__author__= "Pedro Henrique"
__license__= "unlicense"

import os

import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value
    
current_language = arguments["lang"]

if current_language is None:
    # TODO: usar repetiçao        
    env_lang = os.getenv("LANG","").strip()
    if env_lang:
        current_language = env_lang[:5]
    else:
        current_language = input("Choose a language (ex: en_US, pt_BR):")
        
msg = {
    "pt_BR": "Ola, mundo!",
    "en_US": "Hello world!",
    "es_ES": "¡Hola, mundo!",
    "zh_CN": "你好，世界",
    "ar_SA": "مرحبا بالعالم",
}

print(msg[current_language] * int(arguments["count"]))
