class Televisao:
    def __init__(self) -> None:
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


# faz o controle para executar abaixo somente quando for chamada do mesmo arquivo
if __name__ == '__main__':
    # cria instância da classe televisão
    televisao = Televisao()

    print('A televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('A televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('A televisão está ligada: {}'.format(televisao.ligada))

    # liga a televisão
    televisao.power()

    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
