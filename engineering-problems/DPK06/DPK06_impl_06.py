def has_separator(input, separator, index):
    separator_index = 0

    while separator_index < len(separator):
        input_index = index + separator_index

        if input_index >= len(input):
            return False
        if input[input_index] != separator[separator_index]:
            return False

        separator_index += 1

    return True


def create_separator_map(input, separator):
    separator_map = []
    separator_start_map = []
    index = 0

    while index < len(input):
        separator_map.append(False)
        separator_start_map.append(False)
        index += 1

    index = 0

    while index < len(input):
        if has_separator(input, separator, index):
            separator_start_map[index] = True
            separator_index = 0

            while separator_index < len(separator):
                separator_map[index + separator_index] = True
                separator_index += 1

            index += len(separator)
        else:
            index += 1

    return separator_map, separator_start_map


def tokenize(input, separator):
    if separator == "":
        raise ValueError("separator cannot be empty")

    tokens = []
    token = ""
    index = 0
    separator_map, separator_start_map = create_separator_map(input, separator)

    while index < len(input):
        if separator_start_map[index]:
            tokens.append(token)
            token = ""

        if separator_map[index]:
            index += 1
        else:
            token += input[index]
            index += 1

    tokens.append(token)
    return tokens


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
