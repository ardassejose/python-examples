print('Conversor de moedas')
din = float(input('Quanto reais você tem? '))
us = din / 5.11
print('Você tem o equivalente a US${:.2f}'.format(us))
din = float(input('Quanto dólares você tem? '))
us = din * 5.11
print('Você tem o equivalente a R${:.2f}'.format(us))
