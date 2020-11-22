def vetor_list(vetorList): 
    i = 0
    while i < len(vetorList):
        print(vetorList[i])
        i = i + 1

    
vetorList = [1, 4, 9, 22, 18]

# mostrando apenas os números do vetor fora da lista

vetor_list(vetorList)


# outra função com usuário add números
def mostra_vetor():
    lista = []
    while len(lista)<5:
        n = int(input("Digite um numero qualquer: "))
        lista.append(n)
    print(lista)
    

mostra_vetor()
