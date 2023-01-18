pilha = []
i = 0

def push(valor):
    pilha.append(valor)
    
def pop():
    valor = pilha[-1]
    del pilha[-1]
    return valor

push("jonas")
push("caio")
push("lucas")

for i in range(len(pilha)):
    print(pop())