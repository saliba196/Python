#Funções Lambda - permite criar uma função em uma linha só
# lambda argumentos: expressao
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10


#Função MAP - aplica uma função a cada item de uma lista / tupla etc
def dobrar(numero):
    return numero * 2

numeros = [1, 2, 3, 4, 5]
resultado = map(dobrar, numeros)
lista_resultado = list(resultado)

print(lista_resultado)  # Saída: [2, 4, 6, 8, 10]


#Função list - transforma uma tupla em uma list
tupla = (1, 2, 3, 4, 5)
lista = list(tupla)
print(lista)  # Saída: [1, 2, 3, 4, 5]
