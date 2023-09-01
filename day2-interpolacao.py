# coding: utf-8
email_template = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é otimo para resolver
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponiveis!

Preço promocional %(preco).2f
"""
clientes = ['Maria', 'Joao', 'Bruno']
for cliente in clientes:
    print(
        email_template
        % {
            'nome': cliente,
            'produto': 'Caneta',
            'texto': 'Um texto bonito aqui',
            'link': 'https://canetaslegais.com',
            'quantidade': 2,
            'preco': 40.0,
        }
    )
