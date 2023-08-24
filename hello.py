#!/usr/bin/env python3
"""Hello World Multi Lingua

Dependendo do idioma configurado no ambiente, exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada.

Exemplo:
    
    export LANG=pt_BR

Exec.:

    python3 hello.py
    
    ou

    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Fabricio Castro"
__license__ = "Unlicense"

# Dunder = DoubleUnder (__algumacoisa__)
# Comentarios:
# - Serve par informar o uso do script/programa
# - no final da linha/comando serve como uma tag

import os

current_language = os.getenv('LANG', 'en_US')[:5]

msg = 'Hello World'

if current_language == "pt_BR":
    msg = 'Olá Mundo'
elif current_language == "it_IT":
    msg = 'Ciao, Mondo'
elif current_language == "es_SP":
    msg = 'Hola, Mundo'
elif current_language == 'fr_FR':
    msg = 'Boujour Monde'

print(msg)
