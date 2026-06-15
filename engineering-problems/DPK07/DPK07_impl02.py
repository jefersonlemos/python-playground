def _group_items(items, size):
    if items is None or size is None or size <= 0:
        raise ValueError("Error with data")

    grouped_output = []
    current_group = []

    for item in items:
        current_group.append(item)

        if len(current_group) == size:
            grouped_output.append(current_group)
            current_group = []

    if current_group:
        grouped_output.append(current_group)

    return grouped_output


def group(items, size):
    return _group_items(items, size)


def group_by(items, size):
    return _group_items(items, size)


if __name__ == "__main__":
    print(group(["Hi", "Hello", "hey", "who", "are"], 2))
