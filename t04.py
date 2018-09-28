a=int(input())
deliteli=0
for i in range(-a , a+1):
    if (i!=0) and (a%i==0):
        deliteli +=1


if (deliteli<=4) :
    print('Простое число')
else:
    print('Составное число')