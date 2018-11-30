def check(text):
    if type(text) != str:
        raise TypeError
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    storage = []
    for i in text:
        if i in brackets_open:
            storage.append(brackets_open.index(i))
        elif i in brackets_closed:
            if storage and storage[-1] == brackets_closed.index(i):
                storage.pop()
            else:
                return False
    return not storage
