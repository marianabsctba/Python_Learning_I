sair = False
p = 0
names = []
heights = []


def line():
    print("==" * 40)

def menu():
    line()
    print("Bem-vindo ao programa que verifica quais são os alunos mais altos (em comparação com a média)")
    line()
    
def media_heights():
    h_t = 0
    for p in range(len(heights)):
        h_t = h_t + heights[p]  
    m = float(h_t/len(heights))
    return m


def show_list():
    m_t = media_heights()
    print("A média de altura é: ", m_t, "cm.")
    for p in range (len(heights)):
        if heights[p] > m_t:
            line()
            print("Nome/altura dos alunos acima da média: ", names[p],"-", heights[p], "cm.")
            line()

menu()

while not sair: 
    name = input(f"Qual é o nome do  aluno? ").upper().strip()
    if name == "SAIR":
        break
    else:
        names.append(name)
    h= float(input("Qual é a altura do aluno (em cm, sem vírgula)? "))    
    heights.append(h)       

show_list()
