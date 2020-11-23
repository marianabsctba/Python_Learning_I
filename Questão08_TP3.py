import random

def line():
    print("==" * 30)

def menu():
    line()
    print(f"Saiba qual foi o resultado de 100 jogadas de um dado de modo randômico!")
    
def throw_dice(times):
    possible = [0] * 6
    for i in range(0, times):
        throw = random.randrange(0, 6)
        possible[throw-1] += 1
 
    for t in range(0,6):
        line()
        print(f"Número: {t+1} = Vezes: {possible[t]} = Percentual: {round((possible[t]/times) * 100)} %.")


menu()
throw_dice(100)
line()
