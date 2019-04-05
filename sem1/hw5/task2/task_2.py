def drugs(t1, t2, t3, time):
    cook_time = 0
    deal = 0
    injection = 0
    doza = 0
    nark_1 = ''
    nark_2 = ''
    hod = 0
    for i in range(time):
        shag = 0
        if deal == 0 and cook_time < t1:
            cook_time += 1
            nark_1 += 'N'
        elif injection == 0:
            deal += 1
            nark_1 += 'p'
        else:
            nark_1 += '.'

        if deal == t2:
            doza = 1
            cook_time = 0
            deal = 0
            shag = 1

        if doza == 1 and shag == 0:
            deal = 0
            injection += 1
            nark_2 += 'I'
        else:
            nark_2 += '.'

        if injection == t3:
            injection = 0
            doza = 0
            hod += 1
    result = (len(nark_2) - hod * t2) / hod
    print(nark_1)
    print(nark_2)
    return result
