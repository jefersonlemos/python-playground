def _validate_inputs(items, group_size):
    if items is None or group_size is None or group_size <= 0:
        raise ValueError("group_size must be greater than zero")


def _group_recursive(items, group_size):
    if not items:
        return []

    head = items[:group_size]
    tail = items[group_size:]
    return [head] + _group_recursive(tail, group_size)


def group_by(items, group_size):
    _validate_inputs(items, group_size)
    return _group_recursive(list(items), group_size)


if __name__ == "__main__":
    print(group_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(group_by(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 3))
