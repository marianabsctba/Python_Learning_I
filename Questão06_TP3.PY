def user_phrase(l):
    exist = True
    while exist:
        user = str(input("Qual frase você quer digitar? Para parar digite 'sair': ")).lower()
        if user != "sair":        
            l.append(user)
        else:
            exist = False
    return l


def check(l):
    for p in range(len(l)):
        if "eu" in l[p].split(" "):
            print(f"Frase com 'eu': ", l[p])
            

l = []

user_phrase(l)
check(l)
