def revert_list(list):
    list_size = len(list)
    i = 0
    #Creates a list with `list_size` slots so I can add values to [i] when looping
    reverted_list = [None] * list_size
    
    while i < list_size:
        current_position = list_size - i - 1
        reverted_list[i] = list[current_position]
        i += 1
    return reverted_list


# list = [1,2,3,4,5]
list = [5,6,7,8,9]
print(revert_list(list))
