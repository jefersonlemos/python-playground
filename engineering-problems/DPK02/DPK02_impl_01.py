def revert_list(list):
    list_size = len(list)
    i = 0
    reverted_list = list
    print("list", list)
    # print("reverted", reverted_list)
    print("list_size", list_size)
    
    while i < list_size:
        current_position = list_size - i - 1
        print("current_position", current_position)
        print("current_value", list[current_position] )
        
        
        reverted_list[i] = list[current_position]
        print("reverted", reverted_list)
        i += 1
    return reverted_list


# list = [1,2,3,4,5]
list = [5,6,7,8,9]
print(revert_list(list))
