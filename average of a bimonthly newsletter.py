notas = [0, 0, 0, 0]
nbimestre = ["Primeiro", "Segundo", "Terceiro", "Quarto"]
media = 0

for i in range(4):
    notas[i] = int(input('{} bimestre: '.format(nbimestre[i])))
    while notas[i]>10 or notas[i]<0:
        notas[i]= int(input('Numero invalido... {} bimestre: '.format(nbimestre[i])))
    media += notas[i]
    
media /= 4
print('média: {}'.format(media))
if(media<7):
    print('Aluno Reprovado')
else:
    print('Aluno Aprovado')
