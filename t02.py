def calc(x1, operation, x2):
    if operation == '+':
        return (a + b)
    elif operation == '-':
        return (a-b)
    if operation =='*':
        return (a*b)
    elif operation =='/':
        return (a/b)
    else:
        print('Неизвестная операция')



a, oper, b = input().split()
a = int(a)
b = int(b)
print(calc(a, oper, b))

