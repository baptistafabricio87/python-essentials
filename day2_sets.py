# coding: utf-8
cj1 = {1, 2, 3}
cj1
type(cj1)
cj1 = set((1, 2, 3))
type(cj1)
cj1 = set([1, 2, 3])
type(cj1)
cj1 = set('banana')
type(cj1)
get_ipython().run_line_magic('pinfo', 'set')
# set() novo conjunto vazio
# set('banana') novo conjunto com conteudo passado na definição.
cj1
# conjunto não garante ordem, e mantém somente valores unicos, ou seja, não permite repetição de itens.
# exemplos de operações de conjunto
conjunto_a = [1, 2, 3, 4, 5]
conjunto_b = [4, 5, 6, 7, 8]
# União
set(conjunto_a) | set(conjunto_b)
set(conjunto_a).union(set(conjunto_b))
conjunto_a = set([1, 2, 3, 4, 5])
conjunto_b = set([4, 5, 6, 7, 8])
# É recomendado definir o set antes de sua utilização. como feito acima.
# Intersecção
conjunto_a & conjunto_b
conjunto_a.intersection(conjunto_b)
# Diferença - Neste caso é importante verificar a ordem da operação. 
conjunto_a - conjunto_b
conjunto_a.difference(conjunto_b)
conjunto_b - conjunto_a
conjunto_b.difference(conjunto_a)
# Diferença Simetrica - Retorna todos os elementos diferentes entre si.
conjunto_a ^ conjunto_b
conjunto_b ^ conjunto_a
conjunto_a.symmetric_difference(conjunto_b)
conjunto_b.symmetric_difference(conjunto_a)
# Set não servem para armazenar informações, utilizados como objetos de transição, como retirar duplicidades, ou realizar as operações anteriores, união, intersecção, diferença e diferença simetrica.
# Alguns protocolos do objeto Set.
cj1 = set()
# adicionando elementos.
cj1.add(1)
cj1.add(2)
cj1.add(3)
cj1
# Set não permite repetição de elementos, então ao tentar adicionar um elemento já existente o set não é alterado. 
cj1.add(3)
cj1.add(3)
cj1
# Set implementa HASH TABLE, com isso a operação de buscar tem maior performance. Tendo sua operação como 'O de 1' CONSTANTE. 
# Quando não utilizar Set? 
# Quando é permitido duplicidade de elementos. 
# Quando é necessário manter a ordem do objeto. 
# Set não permite acesso aos elementos por indice, pois ele não garante a ordem dos elementos.
cj1[0]
""" ------------------------------------------------------
TypeError            Traceback (most recent call last)
Cell In[54], line 1
----> 1 cj1[0]

TypeError: 'set' object is not subscriptable
"""
# Set não é um objeto subscriptable.
