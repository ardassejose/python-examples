print('Baldes de tintas necessário para pintar sua parede')
lar = float(input('Digite a largura da sua parede em metros: '))
alt = float(input('Digite a altura da sua parede em metros: '))
area = lar * alt
b = area / 2
print('Você irá precisar de {} litros para pintar {}m2'.format(b, area))
