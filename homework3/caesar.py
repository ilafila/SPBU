from caesar_logic import encrypt, decrypt

print('Введите операцию e или d')
variant = str(input())
if variant == 'e':
    print('Введите сдвиг')
    s = int(input())
    print('Введиет текст ')
    t = str(input())
    print(encrypt(s, t))
elif variant == 'd':
    print('Введите сдвиг')
    s = int(input())
    print('Введите текст')
    t = str(input())
    print(decrypt(s, t))
