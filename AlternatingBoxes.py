normal_order = ['B','B','B','B','W','W','W','W']

def swap(liste, position1, position2):
    temp = liste[position1]
    liste[position1] = liste[position2]
    liste[position2] = temp

def alternate_helper(liste, pos1, pos2):
    list_len = pos2 - pos1 + 1
    if(list_len == 2):
        return liste
    if (list_len == 4):
        swap(liste, pos1+1, pos2-1)
        return liste
    swap(liste, pos1+1, pos2-1)
    return alternate_helper(liste, pos1+2, pos2-2)

def alternate(liste):
    return alternate_helper(liste, 0, len(liste) - 1)

def print_list(liste):
    for i in liste:
        print(i, end=' ')
    print("\n")

normal_order = alternate(normal_order)
print_list(normal_order)

