import random


def klava_check(time, probability, time_lasts):
    time_check_new = time // time_lasts
    for i in range(time_check_new):
        if random.randint(1, 10000) <= probability * 100:
            return True
    return False


def konstantin_tests(time, probability, time_lasts, number_sim):
    result = ''
    for i in range(number_sim):
        if klava_check(time, probability, time_lasts):
            result += 'L'
        elif random.randint(1, 10000) <= probability * 100:
            result += 'S'
        else:
            result += 'F'
    return result
