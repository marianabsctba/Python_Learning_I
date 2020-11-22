#prmeira função inverte a ordem de leitura

def vetor(vetorWord):
    vetorWord.reverse()
    return vetorWord

#segunda função inverte palavras e as retira da lista

def inverse_vetor(vetorWord):
    for palavra in vetorWord:
        print(palavra[::-1])

vetorWord = ["morango", "sal", "batata", "flor", "cachorro", "Python", "Infnet", "Borboleta", "Coruja", "Filmes"]

print(vetor(vetorWord))

inverse_vetor(vetorWord)
