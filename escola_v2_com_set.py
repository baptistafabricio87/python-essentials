#!/usr/bin/env python3
"""
Programa para exibir lista de alunos por atividade e sala

Ingles:
    Sala 1: [Miguel, Arthur]
    Sala 2: [Bruno, Davi, Antonio]
-----
Musica:
    Sala 1: [Ivan, Miguel]
    Sala 2: [Davi, Maria, Leticia]
-----
Dança:
    Sala 1: [Valentina, Eloa, Hana]
    Sala 2: [Maria, Leticia, Luiza]
"""

__version__ = '0.1.0'
__author__ = 'Fabricio Castro'


sala_1 = ['Miguel', 'Arthur', 'Ivan', 'Valentina', 'Eloa', 'Hana']
sala_2 = ['Bruno', 'Davi', 'Antonio', 'Maria', 'Leticia', 'Luiza']

aula_ingles = ['Miguel', 'Ivan', 'Valentina', 'Antonio', 'Luiza']
aula_musica = ['Arthur', 'Eloa', 'Hana', 'Davi', 'Leticia']
aula_danca = ['Bruno', 'Maria', 'Hana', 'Valentina', 'Luiza']

atividades = [
    ('Ingles', aula_ingles),
    ('Musica', aula_musica),
    ('Dança', aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, alunos in atividades:

    print(f'\nLista de Alunos - {nome_atividade}')
    print('-' * 40)

    atividade_sala1 = set(sala_1) & set(alunos)
    atividade_sala2 = set(sala_2).intersection(alunos)

    print('Sala 1:', atividade_sala1)
    print('Sala 2:', atividade_sala2)
    print('_' * 40)
