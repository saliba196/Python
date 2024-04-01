#Ex01
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura (metros): '))
imc = peso/altura**2
print(f'Uma pessoa com {peso:} Kg, altura {altura:}m, possui IMC igual a: {imc: }')

#Ex02
Valormili = float
valorM = float(input('Digite o valor em Metros: '))
Valormili = valorM *1000
print(f'O valor em milimetros é : {Valormili:}')


#Ex03
Dias = int(input('Digite o número de dias: '))
Horas = int(input('Digite o número de horas: '))
Minutos = int(input('Digite o número de minutos: '))
segundos = int(input('Digite o número de segundos: '))
totalseg = (Dias*24*60*60 + Horas*60*60 + Minutos*60 + segundos)
print(f'O valor em segundos é: {totalseg:}')

#Ex04
SalarioAtual = float(input('Digite o valor do salário: '))
Aumento = float(input('Digite a porcentagem do aumento do salário: '))
porcAumento = (1+ Aumento/100)
NovoSalario = porcAumento*SalarioAtual
print(f'O novo valor de salário é: {NovoSalario:}') 

#Ex05
TempC = float(input('Digite o valor da temperatura em graus Celsius: '))
TempF = (TempC*1.8 + 32)
print(f'A temperatura em Fahrenheit é: {TempF: }')

#Ex06
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura (metros): '))
imc = peso/altura**2
print(f'Uma pessoa com {peso:} Kg, altura {altura:}m, possui IMC igual a: {imc: }')

#Ex07
ValorProd = float(input('Digite o valor atual do produto: '))
NovoP = ValorProd*0.9 
print(f'O produto com desconto de 10% sai por: {NovoP: }')

#Ex08
Distancia = float(input('Digite a distância que vai percorrer na viagem: '))
Velocidade = float(input('Digite a velocidade média da viagem: '))
Tempo = Distancia/Velocidade
print(f'O tempo de viagem será: {Tempo:}')

#Ex09
Km = float(input('Quantos Kms você percorreu com o carro? '))
Dias = int(input('Quantos dias você usou o carro? '))
preco = (Dias*60)+(Km*0.15)
print(f'O valor total do aluguel a ser pago é de {preco: }')

#Ex10
R1 = float(input('R1: '))
R2 = float(input('R2: '))
R3 = float(input('R3: '))
Denom = (1/R1)+(1/R2) + (1/R3)
R = 1/Denom
print(f'A resistência total é de: {R:}')







