def revert_list(list):
    list_items = 0
    reverted_list = []

    for item in list:
        list_items += 1
    
    r = list_items - 1
    l = 0

    for item in list:
        reverted_list.insert(l, list[r])
        r -= 1
        l += 1

        if r < 0:
            return reverted_list

list = [1,2,3]
print(revert_list(list))