# При построении алгоритма посоветовался с Дмитрием Кривошеем :)
def diff(inp_str):
    if type(inp_str) != str:
        raise TypeError()
    poly = inp_str.split()
    if poly[len(poly) - 1].find("x") == -1:
        poly = poly[:(len(poly)-2)]
    for x in range(len(poly)):
        if poly[x].find("x") != -1:
            if poly[x].find("^") == -1:
                poly[x] += "^1"
            pnmb = poly[x].split("x^")
            if pnmb[0] == '':
                a = int(pnmb[1])
                b = int(pnmb[1]) - 1
            else:
                a = int(pnmb[0]) * int(pnmb[1])
                b = int(pnmb[1]) - 1
            if b == 1:
                poly[x] = str(a) + "x"
            elif b == 0:
                poly[x] = str(a)
            elif a == -1:
                poly[x] = "-x^" + str(b)
            else:
                poly[x] = str(a) + "x^" + str(b)
        if poly[x].find("-") != -1 and len(poly[x]) > 1 and x > 1:
            if poly[x-1] == "+":
                poly[x] = poly[x][1:]
                poly[x-1] = "-"
            else:
                poly[x] = poly[x][1:]
                poly[x-1] = "+"
    return " ".join(poly)

asi = input()
print(diff(asi))