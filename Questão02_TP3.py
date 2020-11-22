#duas soluções diferentes abaixo:

# mostrando apenas os números do vetor fora da lista


def vetor_list(vetorList): 
    i = 0
    while i < len(vetorList):
        print(vetorList[i])
        i = i + 1

    
vetorList = [1, 4, 9, 22, 18]

# outra função com input do usuário

def mostra_vetor():
    lista = []
    while len(lista)<5:
        n = int(input("Digite um numero qualquer: "))
        lista.append(n)
    print(lista)
    

vetor_list(vetorList)
mostra_vetor()
