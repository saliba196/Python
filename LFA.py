def convertDelta(string):
    return string.split(' ')

def step(state, step):
    auxDeltas = []
    for a in deltas:
        if (a[0] == state):
            auxDeltas.append(a)
    for a in auxDeltas:
        if(a[1] == step):
            return a[2]

deltaString = input('Funcoes delta: ')
deltas = convertDelta(deltaString)

startState = input('Estado inicial: ')
finalState = input ('Estado final: ')
actualState = startState
path = input('Insira a String desejada: ')

for a in path:
    actualState = step(actualState, a)
    
if (actualState == finalState):
    print('String aceita')
else:
    print('String rejeitada')