def revert_list(list):
    l = 0
    r = len(list) - 1

    while l < r:
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

    return list

list = [1,2,3,4,5,6,7,8,9,10,11,12]
print(revert_list(list))
