#nome[inicial:final+1:passo]
nome = 'luiza'
print(nome)
print(nome[0])
print(nome[2])
print(nome[3])
print(nome[4])

String2 = 'Ref'
#funções
len(nome) #volta o tamamho da string
nome.count('a') # conta a quantidade de As na string
nome.find('a') # Encontra os o primeiro A na string
nome.replace('a', 'b') #Troca as letras a por b - troca na referência, não na string, para trocar na string é necessário colocar nome = nome.replace('a','b')
nome.upper() #Transforma todo o texto em caixa alta
nome.lower() #Transforma todo o texto em caixa baixa
nome.captalize() #Coloca a primeira letra maiuscula da string
nome.split() #Quebra a string em uma lista - sem argumentos ele quebra no espaço
nome.join() #junta uma lista de palavras
nome.intersection(String2)

Setnome = set(nome) #bom para comparar strings ou achar padrões
SetString2 = set(String2)
S3 = Setnome.intersection(SetString2) #encontra a intersecção entre as strings

i=[5,6,7,8,9,10]
print(i, end='')

#métodos is verificam se a string é alguma dessas coisas
nome.isnumeric()
nome.isalpha()
nome.isspace()

