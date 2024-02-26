import random

min="abcdefghijklmnopqrstuvwxyz"
may=min.upper()
num="1234567890"
sim="[]{}()@*,;/-_¿?.¡!$<#>&+%="

longitud= int(input("de cuantos caracteres desea su contraseña?: "))
base= min + may + num + sim

muestra=random.sample(base,longitud)
pasword="".join(muestra)
print(pasword)
