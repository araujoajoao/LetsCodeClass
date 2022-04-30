## Questão 1. Peça um número e valide se este número é divisível por 5.

numero=int(input('Digite um número: '))
if (numero % 5) == 0:
    print ('Divisível por 5')
else:
    print ('Não é divisível por 5')