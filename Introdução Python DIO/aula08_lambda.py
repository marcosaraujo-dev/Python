# exemplo utilização lambda

def contador_letras(lista): return [len(x) for x in lista]


lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))


def soma(a, b): return a + b


def subtracao(a, b): return a - b


print(soma(5, 10))


print(subtracao(25, 8))

calculadora = {
    'soma': lambda a, b: a+b,
    'subtracao': lambda a, b: a-b,
    'multiplicacao': lambda a, b: a*b,
    'divisao': lambda a, b: a/b,
}

print(type(calculadora))

calcular_soma = calculadora['soma']
calcular_multi = calculadora['multiplicacao']
print('Resultado Soma lambda: {}'.format(calcular_soma(12, 10)))
print('Resultado Multiplicação lambda: {}'.format(calcular_multi(7, 9)))
