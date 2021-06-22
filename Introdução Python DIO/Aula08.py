# importação de módulos, classes e funçõrs anônimas
from aula07_televisao import Televisao
from aula07_calculadora import Calculadora
from aula08_contador_letras import contador_letras
# acesso classe televisão
televisao = Televisao()

print('TV ligada: {}'.format(televisao.ligada))
televisao.power()
print('TV ligada: {}'.format(televisao.ligada))

# Acesso classe calculadora
calculadora = Calculadora(5, 10)
print('Soma: {}'.format(calculadora.soma()))

# acesso metodo contador de letras
lista = ['cachorro', 'gato', 'elefante']
print('Valores contador de letras: {}'.format(contador_letras(lista)))
