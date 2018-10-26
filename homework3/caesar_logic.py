def encrypt(offset, text):
    storage = []
    result = ''
    if type(offset) != int:
        raise TypeError
    for i in text:
        if ord(i) < ord('A') or ord(i) > ord('z'):
            new_number = ord(i)
        elif ord(i) < ord('A') or ord(i) > ord('z') and offset < 0:
            new_number = ord(i) - offset
        else:
            new_number = ord(i) + offset
        storage.append(new_number)
    for j in range(len(storage)):
        if storage[j] > ord('Z') and (storage[j] < (ord('a') + offset)):
            result += chr(storage[j] - 26)
        elif storage[j] > ord('z'):
            result += chr(storage[j] - 26)
        else:
            result += chr(storage[j])
    return result


def decrypt(offset, text):
    storage = []
    result = ''
    if type(offset) != int:
        raise TypeError
    for i in text:
        if ord(i) < ord('A') or ord(i) > ord('z'):
            new_number = ord(i)
        elif ord(i) < ord('A') or ord(i) > ord('z') and offset < 0:
            new_number = ord(i) + offset
        else:
            new_number = ord(i) + offset
        storage.append(new_number)
    for j in range(len(storage)):
        if storage[j] > ord('Z') and (storage[j] < (ord('a') + offset)):
            result += chr(storage[j] - 26)
        elif storage[j] > ord('z'):
            result += chr(storage[j] - 26)
        else:
            result += chr(storage[j])
    return result
