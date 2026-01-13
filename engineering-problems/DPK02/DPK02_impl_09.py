def revert_list(list):
    '''
    impl_09: loop over a list using while, add the values to a temp list and then loop over the temp list starting from the end
    '''
    list_size = len(list)
    temp_list = [None] * list_size
    l = 0
    i = 0

    while i < list_size:
        temp_list[l] = list[i]
        l += 1
        i += 1
    
    l -= 1
    i = 0        
    
    while i < list_size:
        list[i] = temp_list[l]
        l -= 1
        i += 1    

    return list

list = [1,2,3,4]
print(revert_list(list))
