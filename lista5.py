#Ex01
def contar_caracteres(frase):
    contagem = {}
    for caractere in frase:
        if caractere != ' ':
            if caractere in contagem:
                contagem[caractere] += 1
            else:
                contagem[caractere] = 1
    return contagem

frase = input("Digite uma frase: ")
resultado = contar_caracteres(frase)
print(resultado)


# Ex02
def preco_total(frutas, compras):
    total = 0
    for fruta, quantidade in compras.items():
        total += frutas[fruta] * quantidade
    return total


frutas = {'maçã': 2.5, 'banana': 3.0, 'laranja': 4.0, 'uva': 5.5}

compras = {'maçã': 2, 'banana': 1, 'laranja': 3, 'uva': 2}

preco_total_carrinho = preco_total(frutas, compras)
print(f'O preço total do carrinho de compras é: R${preco_total_carrinho:.2f}')

frutas = {fruta: preco for fruta, preco in frutas.items() if preco <= 5.0}
print('Frutas após remoção das que custam mais de R$ 5,00:', frutas)


#Ex03
def verificar_situacao(media):
    if media < 3:
        return 'Reprovado'
    elif media >= 3 and media < 6:
        return 'Exame'
    else:
        return 'Aprovado'

nome = input("Digite o nome do aluno: ")
ra = input("Digite o RA do aluno: ")
media_final = float(input("Digite a média final do aluno: "))

aluno = {
    'Nome': nome,
    'RA': ra,
    'Média Final': media_final,
    'Situação': verificar_situacao(media_final)
}

print("\nInformações do Aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")


#Ex04
pessoas = []
op = 0
print('Op 1 para continuar e -1 para parar')
op = int(input('Op: '))
while(op!=-1):
    nome = input('Nome: ')
    peso = input('Peso: ')
    altura = input('Altura: ')
    IMC = input('IMC')
    pessoa = {
        'Nome': nome,
        'Peso': peso,
        'altura': altura,
        'IMC': IMC
        }
    pessoas.append(pessoa)
    print('Op 1 para continuar e -1 para parar')
    op = int(input('Op: '))

Npessoas = [pessoa['Nome'] for pessoa in pessoas]
Numpessoas = len(Npessoas)
print(f"O numero de pessoas e: {Numpessoas: }")
    
pesos = [pessoa['Peso'] for pessoa in pessoas]
pesoM = sum(pesos)/len(pesos)
print(f"O peso medio das pessoas: {pesoM: } kg")
alturas = [pessoa['Altura'] for pessoa in pessoas]
altura_medio = sum(alturas) / len(alturas)
print(f"Altura média das pessoas: {altura_medio:.2f} m")

IMCs = [pessoa['IMC'] for pessoa in pessoas]
IMCM = sum(IMCs)/len(IMCs)
print(f'IMC medio: {IMCM:}')

#EX05

from itertools import groupby

lista_dicionarios = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Maria', 'idade': 30},
    {'nome': 'Pedro', 'idade': 25},
    {'nome': 'Ana', 'idade': 30}
]

chave = 'idade'

lista_dicionarios.sort(key=lambda x: x[chave])

grupos = groupby(lista_dicionarios, key=lambda x: x[chave])

for chave, grupo in grupos:
    print(f'Grupo {chave}:')
    for item in grupo:
        print(item)
    print()




#Ex07
def verificar_chave(dicionario, chave):
    return chave in dicionario

meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}


chave_verificar = input('Chave a ser verificada: ')

if verificar_chave(meu_dicionario, chave_verificar):
    print(f'A chave "{chave_verificar}" existe no dicionário.')
else:
    print(f'A chave "{chave_verificar}" não existe no dicionário.')


#Ex08
def char_un(string):
    return set(string)

S = input('S: ')
char_set = char_un(S)
print('Caracteres únicos: ')
print(char_set)

#Ex09

def ler_dados_jogador():
    nome = input("Digite o nome do jogador: ")
    partidas = int(input("Digite o número de partidas jogadas: "))
    
    gols_por_partida = []
    for partida in range(1, partidas + 1):
        gols = int(input(f"Digite o número de gols na partida {partida}: "))
        gols_por_partida.append(gols)
    
    total_gols = sum(gols_por_partida)
    
    return {
        'Nome': nome,
        'Partidas': partidas,
        'Gols por Partida': gols_por_partida,
        'Total de Gols': total_gols
    }

# Função para exibir as informações do jogador
def exibir_informacoes_jogador(jogador):
    print("\nInformações do Jogador:")
    for chave, valor in jogador.items():
        if chave == 'Gols por Partida':
            print(f"Gols por Partida: {valor}")
        else:
            print(f"{chave}: {valor}")

# Ler os dados do jogador
jogador = ler_dados_jogador()

# Exibir as informações do jogador
exibir_informacoes_jogador(jogador)


























