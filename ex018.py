from math import sin, cos, tan, radians, ceil
ang = int(input('Insira o valor de um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Seu seno é {}'.format(sen))
print('Seu cosseno é {}'.format(cos))
print('Sua tangente é {}'.format(ceil(tan)))
