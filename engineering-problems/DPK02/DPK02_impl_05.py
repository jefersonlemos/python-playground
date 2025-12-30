def revert_list(list):
    s = len(list) - 1
    r = s 
    l = 0
    for item in list:
        list[l] = list[r]
        l += 1
        r -= 1
    if l == s:
        return list



list = [1,2,3]
print(revert_list(list))


