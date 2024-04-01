#Ex01
def fatorial(numero):
    if(numero == 0):
        return 1 
    else: 
        return numero*fatorial(numero-1)


n = int(input("Qual número você deseja calcular o fatorial? "))
if (n<0):
    print('Não possui fatorial')
else: 
    fatn = fatorial(n)
    print(f'O fatorial de {n:} é {fatn: }')    

#Ex02
def maxnum(*lista):
   return max(lista)

L = input('Lista de elementos separados por espaço: ')
lista = [int(x) for x in L.split(' ')]
maior = maxnum(*lista)
print(f'O maior número é: {maior}')

#Ex02 - alternativo
lista = input('Lista de elementos separados por espaço: ').split()
lista_numeros = list(map(int, lista))
maior = max(map(int, lista))
print(f'O maior número é: {maior}')






#Ex03
def multiplo(numA, numB):
    if(numA%numB == 0 or numB%numA == 0):
        return True
    else:
        return False
A = int(input('N1: '))
B = int(input('N2: '))

mult = multiplo(A,B)
if(mult == True):
    print('São múltiplos')
else:
    print('Não são múltiplos')
    
#Ex04
def calculadora(A,B,OP):
    if(OP == '+'):
        return A + B
    elif(OP == '-'):
        return A - B
    elif(OP == '*'):
        return A*B
    elif(OP == '/'):
        return A/B
    else:
        return 'Operação desconhecida'
    
N1 = int(input('N1: '))
N2 = int(input('N2: '))
OP = input('Operador (Soma + Subtração- Multiplicação * Dvisão /): ')
valor = calculadora(N1,N2,OP)
print(valor)

#Ex05
def maior_palavra(lista):
    maior = ' '
    for p in lista:
        if(len(p) > len(maior)):
            maior = p   
    return maior

palavras = input('Lista de palavras separadas por espaço: ').split()
maior = maior_palavra(palavras)
print(f'A maior palavra é {maior}')


#Ex06
def soma_recursiva(A):
    if(A <= 0):
        return 0
    else:
        return A+ soma_recursiva(A-1)
    

N = int(input('N: '))
soma = soma_recursiva(N)
print(soma)

#Ex07
def fatorial(numero):
    if(numero == 0):
        return 1 
    else: 
        return numero*fatorial(numero-1)
    
def sen_taylor(x):
    for i in range(1,50,2):
        sen = x - (x**i/fatorial(i))
        cos = (1-sen**2)**1/2
        print(f"Calculo {i}, seno = {sen}, cosseno = {cos}")

X = int(input("Insira um valor para X: "))
sen_taylor(X)

