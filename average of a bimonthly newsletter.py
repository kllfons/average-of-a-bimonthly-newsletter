a= int(input('primeiro bimestre:'))
while a>10:
    a= int(input('você digitou errado. primeiro bimestre:'))
b= int(input('segundo bimestre:'))
while b>10:
    b= int(input('você digitou errado. segundo bimestre:'))
c= int(input('terceiro bimestre:'))
while c>10:
    c= int(input('você digitou errado. terceiro bimestre:'))
d= int(input('quarto bimestre:'))
while d>10:
    d= int(input('você digitou errado. quarto bimestre:'))
média=(a+b+c+d)/4
print('média: {}'.format(média))


