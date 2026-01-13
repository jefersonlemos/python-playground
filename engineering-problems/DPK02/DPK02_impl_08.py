def revert_list(list):
    '''
        This one is like impl_05 and impl_03 but it uses recursion instead of a while loop and has a function within another
    '''
    
    def swap_items(list, l, r):
        if l >= r:
            return
        
        list[l], list[r] = list[r], list[l]
        
        swap_items(list, l + 1, r - 1)
    
    swap_items(list, 0, len(list) - 1)
    return list

list = [1,2,3,4]
print(revert_list(list))
