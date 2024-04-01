# Comando input
a = input('Digite seu nome: ') #padrão é salvar o dado como string, para outros tipos é necessários especificar
idade = int(input('Digite a sua Idade: '))
altura = float(input('Digite sua altura: '))

"""Operadores aritméticos
Soma: +
Subtração: -
Multiplicação: *
Divisão: /
Divisão inteira //
Potência: **
Resto: %
""" 

#Comando Print
a = 5
print(a)
#imprimindo uma variável no texto
print('a sua idade é: {}' .format(idade))
print(f'a sua idade é: {idade}')

#Condicionais
a = int(input())
b = int(input())
s = a > 4
if (s):
    c = a+b
    print(c,'= a + b')
elif(a<6):
    c = a*b
    print(c, '= a X b')
else:
    c=b-a
    print(c, '= a - b')

#Laços de repetição
#for i in range(limiteInf, limiteSup, passo)
for i in range(5):
    print(i)
    i = i+1
    
#contagem regressiva
print('Contagem regressiva')
for j in range(10, -1, -1):
    print(j)
    
# for duplo
for l in range(4):
    for S in range(3):
        print('l = ', l, 'S = ', S)
    print(l)
    
#While
a = 0
while(a>=0):
    a = int(input('Digite o valor de a: '))
    
print('Valor inválido.')
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    