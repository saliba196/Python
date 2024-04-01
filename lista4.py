#Ex01
S1 = input('S1: ')
S2 = input('S2: ')

pos = S1.find(S2)
print(f"Encontrado a partir da posição: {pos:}")

#Ex02
S1 = input('S1: ')
S2 = input('S2: ')

Set1 = set(S1)
Set2 = set(S2)
S3 = Set1.intersection(Set2)
print(f"Os caracteres em comum são: {S3:}")

#Ex03
def cont_char(string):
    contagem = {}
    for caractere in string:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
          
            contagem[caractere] = 1
    return contagem
S1 = input('S1: ')
resultado = cont_char(S1)
for caractere, vezes in resultado.items():
    print(f"{caractere}: {vezes}x")

#Ex04


def subst_char(string, caracteres_substituir, caracteres_substitutos):
    for antigo, novo in zip(caracteres_substituir, caracteres_substitutos):
        string = string.replace(antigo, novo)
    return string

S1 = input('S1: ')
S2 = input('S2: ')
S3 = input('S3: ')


if len(S2) == len(S3):
    resultado = subst_char(S1, S2, S3)
    print(f"Resultado da substituição: {resultado}")
else:
    print("Erro: as strings de substituição devem ter o mesmo tamanho.")

#Ex05

def is_palindromo(S1):
    S1 = S1.lower()
    return (S1 == S1[::-1])

S1 = input("S1: ")

if is_palindromo(S1):
    print("é palíndromo")
else: 
    print("Não é palíndromo")
    
#Ex06
def inverter_palavras(string):
    palavras = string.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]  
    return ' '.join(palavras_invertidas) 
S1 = input("S1: ")

texto_invertido = inverter_palavras(S1)
print(texto_invertido)

#Ex07
S1 = input("S1: ")
S1 = S1.split()
for i in S1: 
    if(len(i)>=3):
        print(i)
