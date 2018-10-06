a=int(input())
deliteli=[]
for i in range(-abs(a) , abs(a)+1):
    if (i!=0) and (a%i==0):
        deliteli.append(i)


if len(deliteli)==4:
    print('Простое число')
else:
    print('Составное число')