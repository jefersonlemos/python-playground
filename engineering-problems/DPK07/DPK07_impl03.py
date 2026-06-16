def _group_items(items, group_size):
    if items is None or group_size is None or group_size <= 0:
        raise ValueError("group_size must be greater than zero")

    grouped_items = []
    current_group = []

    for item in items:
        current_group.append(item)

        if len(current_group) == group_size:
            grouped_items.append(current_group)
            current_group = []

    if current_group:
        grouped_items.append(current_group)

    return grouped_items


def group_by(items, size):
    return _group_items(items, size)


if __name__ == "__main__":
    print(group_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(group_by(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 3))
