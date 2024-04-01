#Ex01
solucao = int(input('Digite o PH da solução: '))
if(solucao > 7):
    print('A solução é ácida')
elif(solucao < 7):
    print('A solução é básica')
else:
    print('A solução é neutra')

#Ex02

R = 's'
while(R != 'n' and R!= 'N'):
    R = input('R:')
    if(R == 's' or R == 'S'):
        print('OK, continuando..')
    elif(R != 'n' and R!= 'N'):
        print('Resposta inválida, tente novamente...')
print('Fim do programa')

#Ex03

for i in range(10,-1,-1):
    if(i != 0):
        print(i)
    else:
        print('0 e FOGO!')
        
#Ex04
i=0
n = 1
print("Sequência de Fibonacci até o décimo termo:")
for fibonacci in range (10):
    print(i)
    i = n
    n = i+n

#Ex05
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

print("Números primos entre 1 e 100:")
for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")

#Ex06
num = int(input('Insira um número: '))

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
if(is_prime(num) == True):
    print('É primo')
else:
    print('Não é primo')

#Ex07
valor = int(input('V:'))
if(valor>=100):
    ncem = int(valor/100)
    print(f'{ncem:} notas de 100')
    if(valor>=50):
        aux = valor - ncem*100
        ncinquenta = int(aux/50)
        print(f'{ncinquenta:} notas de 50')
        if(valor>=20):
            aux2 = valor - (50*ncinquenta) - (100*ncem)
            nvinte = int(aux2/20)
            print(f'{nvinte:} notas de 20')
            if(valor>=10):
                aux3 = valor - (20*nvinte) - (50*ncinquenta) - (100*ncem)
                ndez = int(aux3/10)
                print(f'{ndez:} notas de 10')
                if(valor>=5):
                    aux4 = valor - (10*ndez) - (20*nvinte) - (50*ncinquenta) - (100*ncem)
                    n5 = int(aux4/5)
                    print(f'{n5:} notas de 5')
                    if(valor>=2):
                        aux5 = valor - (5*n5) - (10*ndez) - (20*nvinte) - (50*ncinquenta) - (100*ncem)
                        n2 = int(aux5/2)
                        print(f'{n2:} notas de 2')
total = (2*n2) + (5*n5) + (10*ndez) + (20*nvinte) + (50*ncinquenta) + (100*ncem)
print(f'resgate total de {total:}')

#Ex08
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura (metros): '))
imc = peso/altura**2

print(f'Uma pessoa com {peso:} Kg, altura {altura:}m, possui IMC igual a: {imc: } e se enquadra no status')

if(imc < 18.5):
    print('Abaixo do Peso')
    
elif(imc>= 18.5 and imc<=24.9):
    print('Peso Normal')
    
elif(imc>= 25 and imc<= 29.9):
    print('Sobrepeso')

elif(imc>= 30 and imc<=34.9):
    print('Obesidade')
    
elif(imc>= 35 and imc<= 39.9):
    print('Obesidade Grau II')

elif(imc>= 40):
    print('Obesidade Grau III')
    
    
#Ex09
def Armstrong(NumS, NumF):
    #aqui teriamos que ter um for do numero de dígitos no número então precisamos de uma função que conte o número de dígitos no número pra função 
    pot1 = NumS
    pot2 = 
    soma = pot1 + pot2
    if(NumF = soma):
        return True
    else:
        return False

NumS = input('N:')
NumF = float(NumS)

if(Armstrong(NumS, NumF) == True):
    print("É número de Armstrong")
else:
    print("Não é número de Armstrong")





