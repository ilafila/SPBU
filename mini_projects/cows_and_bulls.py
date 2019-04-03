import random


def bull_count(secret_number, guess):
    b = 0
    for i in range(len(secret_number)):
        if secret_number[i] == guess[i]:
            b += 1
    return b


def cow_count(secret_number, guess):
    c = 0
    for i in range(len(secret_number)):
        for j in range(0, len(guess)):
            if i != j and secret_number[i] == guess[j]:
                c += 1
    return c


def get_secret_number(n_count):
    storage = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = ''
    for i in range(n_count):
        k = random.randrange(len(storage))
        result += str(storage[k])
        storage.remove(storage[k])
    return result


def is_game_over(secret_number, guess):
    return secret_number == guess


print('Я загадал число')
sec = get_secret_number(4)
print('Введите число')
word = input()

while not is_game_over(sec, word):
    print('Количество быков')
    print(bull_count(sec, word))
    print('Количество коров')
    print(cow_count(sec, word))
    print('Введите число')
    word = input()
