def add_element(l):
   for valor in list(range(1, 6)):
    lista.append(valor)
    return l

def verify_element_3(l):        
    if 3 in l:
        print("O elemento '3' está na lista e será removido!")
        l.remove(3)
    else:
        print("O elemento '3' não está na lista")
    return l

def verify_element_6(l):
    if 6 in l:
        print("O elemento '6' está na lista...")
        l.remove(6)
    else:
        print("O elemento '6' não está na lista...")
    print("Essa é a lista com o elemento retirado:", l)
    return l

def print_size(l):
    print(f"O número de elementos atual da lista é {len(l)}.")    
    
def change_element(l):
    l[3] = 6
    print(f"Essa é a lista com o último elemento trocado: {l}.")
    

l = []

add_element(l)
verify_element_3(l)
verify_element_6(l)
print_size(l)
change_element(l)
