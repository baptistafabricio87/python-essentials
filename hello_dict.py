#!/usr/bin/env python3
"""Hello World Multi Lingua

Dependendo do idioma configurado no ambiente, exibe a mensagem correspondente.

Como usar:
    Tenha a variavel LANG devidamente configurada.

Exemplo:
    export LANG=pt_BR

Exec.:
    python3 hello.py
"""
__version__ = '0.0.1'
__author__ = 'Fabricio Castro'
__license__ = 'Unlicense'

import os

current_language = os.getenv('LANG', 'en_US')[:5]

msg = {
    'en_US': 'Hello, World!',
    'pt_BR': 'Olá, Mundo!',
    'es_SP': 'Hola, Mondo!',
    'it_IT': 'Ciao, Mondo!',
    'fr_FR': 'Bonjour, Monde!'
}

print(msg[current_language])
