def line():
    print("\033[1;34m\==\033[0;0m"* 15)

def read_vector():
    t = int(input("Quantos números quer incluir na lista?: "))
    l = []
    while len(l) < t:
            number = float(input("Digite o número da lista: "))
            l.append(number)
    
    print(f"Número de zeros na lista: {l.count(0)}")

line()
read_vector()
line()
