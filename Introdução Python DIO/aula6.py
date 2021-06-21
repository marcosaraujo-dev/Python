# Aula 6
# conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

# conjunto1.add(5)
# conjunto1.discard(2)

conjunto_uniao = conjunto1.union(conjunto2)
print('união: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto1.difference(conjunto2)
print('conjunto Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))


conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('conjunto Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença Simétrica]: {}'.format(conjunto_diff_simetrica))


conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
# retorna true ou false se as informações do primeiro conjunto está dentro do segundo
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A [e subconjunto de B: {}'.format(conjunto_subset))

# retorna true ou false se as informações dentro do conjunto B possui todos os elementos do conjunto a
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

# |Conjuntos os vaslores nunca se repetem
conj = {1, 2, 2, 1, 4, 5}
print('conjunto: {}'.format(conj))

# exemplo remover duplicidades de uma lista
lista = ['cachorro', 'gato', 'cachorro', 'elefante', 'gato']
# conjuntos não possuem duplicidades
conjunto_animais = set(lista)
print('conjunto animais:{}'.format(conjunto_animais))

lista_animais = list(conjunto_animais)
print('a lista de animais: {}'.format(lista_animais))
