def rotate(l):
    l.insert(0, l.pop(len(l)-1))


a = [1, 2, 3]
rotate(a)
print(a)
