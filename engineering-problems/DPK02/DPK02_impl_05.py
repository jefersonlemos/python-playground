def revert_list(list):
    l = 0
    r = len(list) - 1

    while l < r:
        list[l] = list[r]
        l += 1
        r -= 1

    return list

list = [1, 2, 3, 4]
print(revert_list(list))
