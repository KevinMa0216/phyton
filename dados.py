import random
valor_minimo=1
valor_maximo=6

jugar_otra_vez="si"

while jugar_otra_vez == "si" or jugar_otra_vez=="s":
    print("tirando dados...")
    print("has sacado: ")
    print(random.randint(valor_minimo,valor_maximo))
    print(random.randint(valor_minimo,valor_maximo))
    jugar_otra_vez= input("Deseas volver a tirar? ")