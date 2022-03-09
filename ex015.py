print('Calculadora de aluguel de carro')
nome = str(input('Seja bem vindo aos AlugaCar. Insira seu nome: '))
print('Olá {}, nossa diária custa R$250'.format(nome))
alug = int(input('Quantos dias você deseja alugar um carro? '))
d = 250
print('{}, você irá pagar R${} para usar por {} dias'.format(nome, alug*d, alug))
print('Caso tenha interesse, entre em contato conosco. Até mais!')
