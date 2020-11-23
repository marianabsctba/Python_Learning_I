ef show_list(l):
    print("Veja a lista abaixo. Se nada constar é porque está vazia:")
    for x in range(len(l)):
        print(f"Lista: {l[x]}")

def add_item(l):
    l.append(input("Inclua um item na lista: "))
    print("Você incluiu um item na lista!")

def remove_item(l):
    user = input("Item a ser removido: ")
    if user in l:
        l.remove(user)
        print("O item foi removido.")
    else:
        print("O item não está na lista.")

def erase_list(l):
    lista.clear()
    print("A lista foi removida")
    
def menu():
    while True:
        print(""" =========MENU=========

    1] Mostrar a lista
    2] Incluir na lista
    3] Remover da lista
    4] Apagar todos os elementos da lista
    5] Sair do programa
        
        """)
        
        option = input("Número da opção desejada: ")
        
        if '1' == option:
            show_list(l)
        elif '2' == option:
            add_item(l)
        elif '3' == option:
            remove_item(l)
        elif '4' == option:
            erase_list(l)
        elif '5' == option:
            print("Programa finalizado. Volte sempre.")
            break        
        else:
            print("A operação não existe.")
l = []
            
menu()

