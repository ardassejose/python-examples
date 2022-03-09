from math import sqrt, trunc
print('Catetos e Hipotenusa')
b = (int(input('Digite o valor do cateto: ')))
c = (int(input('Digite o valor do outro cateto: ')))
hip = sqrt((b**2)+(c**2))
print('A hipotenusa vale {}'.format(trunc(hip)))
