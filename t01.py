def rotate(l):
    b = a.copy()
    b.insert(0, b.pop(len(l)-1))
    return b


a = [1, 2, 3]
rotate(a)
print(a, rotate(a))
