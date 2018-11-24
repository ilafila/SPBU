def drugs(t1, t2, t3, time):
    flag1 = 0
    flag2 = 0
    flag3 = 0
    doza = 0
    nark_1 = ''
    nark_2 = ''
    hod = 0
    for i in range(time):
        shag = 0
        if flag2 == 0 and flag1 < t1:
            flag1 += 1
            nark_1 += 'N'
        elif flag3 == 0:
            flag2 += 1
            nark_1 += 'p'
        else:
            nark_1 += '.'

        if flag2 == t2:
            doza = 1
            flag1 = 0
            flag2 = 0
            shag = 1

        if doza == 1 and shag == 0:
            flag2 = 0
            flag3 += 1
            nark_2 += 'I'
        else:
            nark_2 += '.'

        if flag3 == t3:
            flag3 = 0
            doza = 0
            hod += 1
    result = (len(nark_2) - hod * t2) / hod
    print(nark_1)
    print(nark_2)
    return result
