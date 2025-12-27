def revert_list(list,l,r):
    if r < 0:
        print("coco")
        return reverted_list
    else:
        reverted_list[l] = 1
        l += 1
        r -= 1
        return l,r

def thing(list,l,r):
    revert_list(list,l,r)
    l += 1
    r -= 1
    return thing(list,l,r)


list = [5,6,7,8]
list_size = len(list)
reverted_list = [None] * list_size
l = 0
r = list_size - 1

print(thing(list,l,r))