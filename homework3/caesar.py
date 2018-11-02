from caesar_logic import encrypt, decrypt

print('Введите операцию:зашифровать(e) или расшифровать(d)')
variant = input()
if (variant != 'e') and (variant != 'd'):
    raise ValueError('Введите e или d')
print('Введите ключ')
key = int(input())
print('Введите текст')
answer = input()
if variant == 'e':
    print(encrypt(key, answer))
else:
    print(decrypt(key, answer))
