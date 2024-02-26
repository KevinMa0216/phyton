num=int(input("Ingrese un numero: "))
pen=1
ult=1
if num==1:
    print(0)
elif num==2:
    print (0,1)
elif num==3:
    print (0,1,1,)
else:
    print(0,1,1, end=" ")
    for i in range(num-3):
        nuevo=ult+pen
        print(nuevo, end=" ")
        pen=ult
        ult=nuevo