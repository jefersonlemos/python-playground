def _validate_inputs(items, group_size):
    if items is None or group_size is None or group_size <= 0:
        raise ValueError("group_size must be greater than zero")


def group_by(items, group_size):
    _validate_inputs(items, group_size)

    iterator = iter(items)
    grouped_items = []

    while True:
        current_group = []

        for _ in range(group_size):
            try:
                current_group.append(next(iterator))
            except StopIteration:
                break

        if not current_group:
            break

        grouped_items.append(current_group)

        if len(current_group) < group_size:
            break

    return grouped_items


if __name__ == "__main__":
    print(group_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(group_by(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 3))
