def gera_CPF():
    import random
    cpf = [random.randint(0,9) for i in range(9)]
    soma = 0
    for i, digito in enumerate(cpf, start=1):
        soma += digito * (11 - i)
    dig1 = (11 - (soma % 11)) if (soma % 11) >= 2 else 0
    cpf.append(dig1)
    soma = 0
    for i, digito in enumerate(cpf, start=1):
        soma += digito * (12 - i)
    dig2 = (11 - (soma % 11)) if (soma % 11) >= 2 else 0
    cpf.append(dig2)
    
    return ''.join(map(str,cpf))

def verifica_CPF(cpf):
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * len(cpf):
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i])*(10-i)
    dig1 = (11 - (soma % 11)) if (soma%11)>=2 else 0
    soma = 0
    for i in range(10):
        soma+= int(cpf[i]) * (11-i)
    dig2 = (11 - (soma % 11)) if (soma % 11) >=2 else 0
    if dig1 == int(cpf[9]) and dig2 == int(cpf[10]):
        return True
    else:
        return False

op = 0
while(op != -1):
    print('******* Digite 1 para criar um novo CPF ou 2 para verificar se um CPF existe, se quiser sair do programa digite -1 *******')
    op = int(input('Opção:'))
    if(op == 1):
        novoCPF = gera_CPF()
        print(f' O cpf gerado é: {novoCPF}')
    elif (op == 2):
        cpfVer = input('Insira o CPF que deseja verificar (apenas os números): ')
        real = verifica_CPF(cpfVer)
        if(real == True):
            print('O CPF digitado é válido')
        else:
            print('O CPF digitado não é válido')