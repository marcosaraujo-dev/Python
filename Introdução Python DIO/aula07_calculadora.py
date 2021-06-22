# metodos, funções e classes

def soma(a, b):
    return a+b


def subtracao(a, b):
    return a-b


def multiplicacao(a, b):
    return a*b


def divisao(a, b):
    return a/b


print('Soma: {}'.format(soma(7, 9)))
print('subtração: {}'.format(subtracao(12, 5)))
print('Multiplicação: {}'.format(multiplicacao(5, 9)))
print('Divisão: {}'.format(divisao(38, 8)))

# metodo 01 de criação de classe e utilização


class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


# controle para ser chamada essa execução abaixo apenas apenas quando for do proprioo arquivo
if __name__ == '__main__':
    calc = Calculadora(10, 2)

    print('Soma classe:{}'.format(calc.soma()))
    print('Subtração classe:{}'.format(calc.subtracao()))
    print('Multiplicação classe:{}'.format(calc.multiplicacao()))
    print('Divisão classe:{}'.format(calc.divisao()))


# metodo 02 de criação de classe e utilização
class Calculadora02:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


# controle para ser chamada essa execução abaixo apenas apenas quando for do proprioo arquivo
if __name__ == '__main__':
    calc = Calculadora02()

    print('Soma classe 02:{}'.format(calc.soma(10, 7)))
    print('Subtração classe 02:{}'.format(calc.subtracao(15, 8)))
    print('Multiplicação classe 02:{}'.format(calc.multiplicacao(7, 9)))
    print('Divisão classe 02:{}'.format(calc.divisao(49, 7)))
