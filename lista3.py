#Ex01
reais = []
for i in range(10):
  n = float(input(f'Digite o {i+1}º valor: '))
  reais.append(n)
# Mostrando os números na ordem inversa
print("Números reais na ordem inversa:")
for j in range(9, -1, -1):
  print(reais[j])

#Ex02
l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
l2 = ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
l3 = l1 + l2

#Pedindo para o usuário montar a lista
l4 = []
l5 = []
for i in range(5):
  n = input(f"Digite o {i+1}º elemento da lista: ")
  l4.append(n)
for j in range(5):
  n2 = input(f"Digite o {j+1}º elemento da lista: ")
  l5.append(n2)
l6 = l4 + l5
print(l6)

#Ex03
T = [-10, -8, 0, 1, 2, 5, -2, -4]
tempmin = min(T)
tempmax = max(T)
tempMed = sum(T) / len(T)
print(f'Temperatura máxima: {tempmax},'
      f'Temperatura mínima: {tempmin},'
      f'Temperatura média: {tempMed}')

#Ex04
l1 = []
for i in range(20):
  n = int(input(f"Digite o {i+1}º elemento da lista: "))
  l1.append(n)
pares = []
impares = []
for j in range(20):
  if(l1[j] % 2 == 0):
    pares.append(l1[j])
  else:
    impares.append(l1[j])

print(l1)
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')

#Ex04 um pouco mais elegante: 
l1 = []
for i in range(5):
    n = int(input(f"Digite o {i + 1}º elemento da lista: "))
    l1.append(n)

pares = []
impares = []
for num in l1:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(l1)
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')

#Ex05
A1 = []
A2 = []
A3 = []
A4 = []
A5 = []

for i in range(4):
    nota = float(input(f'Insira a {i+1}ª nota do aluno 1: '))
    A1.append(nota)
for j in range(4):
    nota = float(input(f'Insira a {j+1}ª nota do aluno 2: '))
    A2.append(nota)
for k in range(4):
    nota = float(input(f'Insira a {k+1}ª nota do aluno 3: '))
    A3.append(nota)
for o in range(4):
    nota = float(input(f'Insira a {o+1}ª nota do aluno 4: '))
    A4.append(nota)
for m in range(4):
    nota = float(input(f'Insira a {m+1}ª nota do aluno 5: '))
    A5.append(nota)

media1 = sum(A1) / len(A1)
media2 = sum(A2) / len(A2)
media3 = sum(A3) / len(A3)
media4 = sum(A4) / len(A4)
media5 = sum(A5) / len(A5)

medias = [media1, media2, media3, media4, media5]
print(f'A média do aluno 1 é: {media1}')
print(f'A média do aluno 2 é: {media2}')
print(f'A média do aluno 3 é: {media3}')
print(f'A média do aluno 4 é: {media4}')
print(f'A média do aluno 5 é: {media5}')

for a in range(5):
    if medias[a] >= 7:
        print(f'Aluno {a+1} está aprovado')


#Ex06
def soma_quadrados(lista):
  return sum([num ** 2 for num in lista])

numeros = []
for i in range(5):
  num = int(input(f"Digite o {i+1}º número: "))
  numeros.append(num)
resultado = soma_quadrados(numeros)
print(f"A soma dos quadrados dos números é: {resultado}")

#Outra opção de EX06
quadrados = [i**2 for i in range(4)]
somaquad = sum(quadrados)
print(somaquad)

#Ex07
l10 = []
for j in range(4):
    num = int(input(f"Digite o {j + 1}º número: "))
    l10.append(num)

impares = [num for num in l10 if num % 2 != 0]
print(impares)

#Ex08
def string_mais_longa(lista_strings):
    return max(lista_strings, key=len)
  
strings = []
for i in range(5):
    string = input(f"Digite a {i+1}ª string: ")
    strings.append(string)

mais_longa = string_mais_longa(strings)
print(f"A string mais longa é: {mais_longa}")

