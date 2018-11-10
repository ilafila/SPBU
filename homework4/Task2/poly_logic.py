def diff(text):
    if type(text) != str:
        raise TypeError()
    pol = text.split()
    if pol[len(pol) - 1].find("x") == -1:
        pol = pol[:(len(pol)-2)]
    for i in range(len(pol)):
        if pol[i].find("x") != -1:
            if pol[i].find("^") == -1:
                pol[i] += "^1"
            new_pol = pol[i].split("x^")
            if new_pol[0] == '':
                a = int(new_pol[1])
                b = int(new_pol[1]) - 1
            else:
                a = int(new_pol[0]) * int(new_pol[1])
                b = int(new_pol[1]) - 1
            if a == -1:
                pol[i] = "-x^" + str(b)
            elif b == 0:
                pol[i] = str(a)
            elif b == 1:
                pol[i] = str(a) + "x"
            else:
                pol[i] = str(a) + "x^" + str(b)
    return " ".join(pol)
