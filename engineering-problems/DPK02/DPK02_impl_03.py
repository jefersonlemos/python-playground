list = [5,6,7,8,9,10,11,12,13,14,15]
list_size = len(list)

left_list_item = 0
right_list_item = list_size
reverted_list = [None] * list_size

def revert_list(list):
    last_list_item = list_size - 1
    left_list_item += 1
    right_list_item -= 1
    reverted_list[left_list_item] = list[right_list_item]
    return revert_list(list)
    
print(revert_list(list))