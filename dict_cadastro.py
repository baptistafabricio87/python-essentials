#!/usr/bin/env python3
"""Dicionario de Cadastro de Produto"""

produto = {
    'nome': 'Caneta',
    'cores': ['azul', 'preta'],
    'preco': 3.23,
    'dimensao': {
        'altura': 12.1,
        'largura': 0.8,
    },
    'em_estoque': True,
    'codigo': 45678,
    'codebar': None,
}

cliente = {
    'cod': '123',
    'nome': 'Fabricio',
}

compra = {
    'cliente': cliente,
    'produto': produto,
    'quantidade': 3,
}
