import random

num= random.randint(1,100)
intentos=0

jugando= True
print("Adivine un numero del 1 al 100: ")

while jugando:
    intentos +=1
    eleccion= int(input("Dime un numero: "))
    if eleccion== num:
        print("Has acertado. Tuviste un total de ", intentos, "intentos")
        jugando=False
    elif eleccion>num:
        print("el numero que escribiste es mas alto. Llevas ", intentos, "intentos.")
    elif eleccion<num:
        print("el numero que escribiste es mas pequeño. Llevas ", intentos, "intentos.")
