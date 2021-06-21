# aula sobre condicionais
a = int(input('Nota Primeiro Bimestre: '))
if a > 10:
    a = int(input('Nota do primeiro bimestre não pode ser maior que 10: '))

b = int(input('Nota Segundo Bimestre: '))
if b > 10:
    b = int(input('Nota do segundo bimestre não pode ser maior que 10: '))
c = int(input('Nota Terceiro Bimestre: '))
if c > 10:
    c = int(input('Nota do terceiro bimestre não pode ser maior que 10: '))
d = int(input('Nota Quarto Bimestre: '))
if d > 10:
    d = int(input('Nota do quarto bimestre não pode ser maior que 10: '))

media = (a + b + c + d) / 4
print('media das notas digitadas: {}'.format(media))

if media > 7:
    print('Aprovado')
elif media >= 5 and media <= 7:
    print('Aprovado Reforço')
elif media >= 2 and media < 5:
    print('recuperação')
else:
    print('reprovado')

# metodo


def par_ou_impar(numero):
    if numero % 2 == 0:
        return '{} é par'.format(numero)
    else:
        return '{} é impar'.format(numero)
    return 'zero é nulo'


print(par_ou_impar(0))
