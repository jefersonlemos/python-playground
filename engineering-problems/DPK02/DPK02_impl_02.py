def revert_list(list):
    list_size = len(list)
    reverted_list = [None] * list_size
    i = list_size - 1

    for item in list:
        reverted_list[i] = item
        
        if i == 0:
            return reverted_list
        else:
            i -= 1

list = [5,6,7,8,9,10,11,12,13,14,15]
print(revert_list(list))
