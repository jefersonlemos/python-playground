def _validate_inputs(items, group_size):
    if items is None or group_size is None or group_size <= 0:
        raise ValueError("group_size must be greater than zero")


def group_by(items, group_size):
    _validate_inputs(items, group_size)

    grouped_items = []
    current_group = []

    for index, item in enumerate(items, start=1):
        current_group.append(item)

        if index % group_size == 0:
            grouped_items.append(current_group)
            current_group = []

    if current_group:
        grouped_items.append(current_group)

    return grouped_items


if __name__ == "__main__":
    print(group_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(group_by(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 3))
