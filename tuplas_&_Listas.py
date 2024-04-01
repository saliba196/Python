#tuplas - imutáveis



#listas
l = ['Thiago', "Luiza", 'Paula']
# l = ll copia e os ponteiros apontam para o mesmo lugar
# l = ll[:0] copia de verdade e alterações em uma não mudam o outro

""" Em python todas as varíaveis são objetos que possuem métodos e atributos;
Métodos de lista: 
    append() - Adiciona elementos no final (sempre)
    count() - Conta o número de elementos
    insert() - Adiciona elementos na posição desejada
    pop() - Remove elemento do topo
    remove() - Remove o primeiro elemento correspondente a busca

Funções: 
    sum () - Devolve soma
    max () - Devolve valor máximo
    min() - Devolve o valor mínimo
    len() - Qtd de elementos

Junção de listas: listão = nomes + Sobrenomes

    """
nome = ['Luiza', 'Araujo', 'de', 'Oliveira', 'Caram', 'Saliba']

for i in range(3): 
   print(nome[i])
k = 0 
for i in nome: 
   print(i)
   
for i in nome:
    print(k, '.', i)
    k = k +1
    
nomes = ['Luiza', 'Maria Eduarda']
sobrenomes = ['Saliba', 'Fonseca']

for i,j in zip(nomes, sobrenomes):
    print(i, ',', j)
    
    
xx2 = [i**2 for i in range(4)]
print(xx2)


Num_Ate_20 = [i for i in range(1,21)]
pares = [i for i in range(1,21) if (i%2 == 0)]

    