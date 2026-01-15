def revert_list(list):
    '''
    #TODO - a recursion that gets the next number based on index and add it to the left
    '''

    def recursion(i, reverted_list):
        if i >= len(list):
            return reverted_list
        
        reverted_list.insert(0, list[i])
        return recursion(i + 1, reverted_list)
    
    return recursion(0, [])




list = [1,2,3,4]
print(revert_list(list))
