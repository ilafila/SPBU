from task_1 import klava_check, konstantin_tests

time = 90
probability = 11
time_lasts = 17
number_sim = 1000
klava_check(90, 11, 17)
output = konstantin_tests(90, 11, 17, 1000)
print(output)
k = 0
for j in output:
    if j == 'S':
        k += 1
print('Вероятность гачисходки:', k / number_sim * 100, '%')
