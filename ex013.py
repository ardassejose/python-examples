print('Reajuste Salarial')
salario = float(input('Insira o valor do seu salário atualmente: R$'))
rjst = salario + (salario*0.15)
print('Parabéns! Seu salário ganhou um aumento de 15%\nAgora ele corresponde a R${:.2f}. Aproveite!'.format(rjst))