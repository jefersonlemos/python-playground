def revert_list(list):
    '''
    #TODO - This is done but looks like the solution 06 but just added the for loop
    What's the difference ? How to do it without the while ?
    '''

    l = 0
    r = len(list) - 1 
    c = 0
    n = 1

    for item in list:
        print(item, list)
        
        for item in range(l,r):
            list[c], list[n] = list[n], list[c]
            c += 1
            n += 1
        c = 0
        n = 1
        # l += 1
        r -= 1
    return list

list = [1,2,3,4]
print(revert_list(list))
