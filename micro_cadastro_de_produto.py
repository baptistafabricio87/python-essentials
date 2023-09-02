#!/usr/bin/env python3
"""Cadastro de Produto"""
__versio__ = '0.1.0'
__author__ = 'Fabricio Castro'

# from pprint import pprint
from dict_cadastro import compra

# pprint(compra)

total_compra = compra['quantidade'] * compra['produto']['preco']

print(
    f"\nCliente {compra['cliente']['nome']} "
    f"comprou {compra['quantidade']} unidades "
    f"de {compra['produto']['nome']} "
    f'e pagou o total de {total_compra}\n'
)
