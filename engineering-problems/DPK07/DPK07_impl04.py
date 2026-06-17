def group_items(items, size):
    if items is None or size is None or size <= 0:
        raise ValueError("group_size must be greater than zero")

    grouped_items = []
    start = 0
    total_items = len(items)

    while start < total_items:
        end = start + size
        current_group = []
        index = start

        while index < end and index < total_items:
            current_group.append(items[index])
            index += 1

        grouped_items.append(current_group)
        start = end

    return grouped_items

def group_by(items, size):
    return group_items(items, size)


if __name__ == "__main__":
    print(group_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(group_by(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 3))
