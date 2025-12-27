def organize_list(list,l,r):
    reverted_list[l] = list[r]
    return l,r

def revert_list(list,l,r):
    organize_list(list,l,r)
    l += 1
    r -= 1

    if r < 0:
        return reverted_list
    return revert_list(list,l,r)


list = [5,6,7,8,9,10,11,12,13,14,15]
list_size = len(list)
reverted_list = [None] * list_size
l = 0
r = list_size - 1

print(revert_list(list,l,r))