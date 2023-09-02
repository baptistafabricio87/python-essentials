#!/usr/bin/env python3
"""
Programa para exibir lista de alunos por atividade e sala com dict

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
__version__ = '0.1.3'
__author__ = 'Fabricio Castro'


# sala_1 = ['Miguel', 'Arthur', 'Ivan', 'Valentina', 'Eloa', 'Hana']
# sala_2 = ['Bruno', 'Davi', 'Antonio', 'Maria', 'Leticia', 'Luiza']

# aula_ingles = ['Miguel', 'Ivan', 'Valentina', 'Antonio', 'Luiza']
# aula_musica = ['Arthur', 'Eloa', 'Hana', 'Davi', 'Leticia']
# aula_danca = ['Bruno', 'Maria', 'Hana', 'Valentina', 'Luiza']

salas = {
    'Sala_1': {'Miguel', 'Arthur', 'Ivan', 'Valentina', 'Eloa', 'Hana'},
    'Sala_2': {'Bruno', 'Davi', 'Antonio', 'Maria', 'Leticia', 'Luiza'},
}

atividades = {
    'Ingles': {'Miguel', 'Ivan', 'Valentina', 'Antonio', 'Luiza'},
    'Musica': {'Arthur', 'Eloa', 'Hana', 'Davi', 'Leticia'},
    'Dança': {'Bruno', 'Maria', 'Hana', 'Valentina', 'Luiza'},
}

# Listar alunos em cada atividade por sala

for atividade, aluno in atividades.items():

    print(f'\nLista de Alunos - {atividade}')
    print('-' * 40)

    atividade_sala1 = set(salas['Sala_1']) & set(aluno)
    atividade_sala2 = set(salas['Sala_2']).intersection(aluno)

    print('Sala 1:', atividade_sala1)
    print('Sala 2:', atividade_sala2)
    print('_' * 40, '\n')
