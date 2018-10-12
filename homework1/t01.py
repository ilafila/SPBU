def rotate(l):
    if len(origin_list)==0:
        return origin_list
    new_list = l.copy()
    new_list.insert(0, new_list.pop(len(l)-1))
    return new_list


origin_list = []
rotate(origin_list)
print(origin_list, rotate(origin_list))
