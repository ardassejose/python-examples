import random
print('Quem irá apagar o quadro?')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('Quem irá apagar o quadro será {}. Que alegria!'.format(escolhido))