print('Supermercado Preço Top')
total = float(input('Qual o preço total de suas compras? R$'))
desc = total * 0.05
print('Parabéns! Você ganhou 5% de desconto, agora você apenas paga R${:.2f}'.format(total-desc))
