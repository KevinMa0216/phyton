def es_primo(n):
 for x in range(2, int(n**0.5)+1):
  if n % x == 0:
   return False
 return True

def lista_primos(n):
 primos = [2,]
 for i in range(3,n,2):
  if es_primo(i):
   primos.append(i)
 return primos
print(lista_primos(int(input("hasta que numero desea ver los primos?: "))))
