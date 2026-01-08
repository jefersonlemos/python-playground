def revert_list(list):
    l = 0
    r = len(list) - 1
    c = 0
    n = 1
    while n <= r:
        '''
        #TODO - Next solution
        instead of switching l with r, where l is the extreme left and r is the extreme right
        it will now move l one by one, for instance:
        list = 1,2,3,4
        1 - 2,1,3,4 ; 2,3,1,4 ; 2,3,4,1
        2 - 3,2,4,1 ; 3,4,2,1 ; 
        3 - 4,3,2,1
        4 - r equals l -> end
        the numbers on the left side will move to the end of the list one-by-one
        with no extra lists
        '''
        list[c], list[n] = list[n], list[c]

        c += 1
        n += 1

        if n > r:
            c = 0
            n = 1
            l += 1
            r -= 1

    return list

list = [1,2,3,4,5,6,7,8,9,10]
print(revert_list(list))
