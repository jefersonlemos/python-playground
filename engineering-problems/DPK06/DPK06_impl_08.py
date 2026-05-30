def copy_text(input, start_index, end_index):
    text = ""
    index = start_index

    while index < end_index:
        text += input[index]
        index += 1

    return text


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


def find_first_separator(input, separator):
    index = 0
    
    while index < len(input):
        if has_separator(input, separator, index):
            return index

        index += 1

    return -1


def tokenize(input, separator):
    if separator == "":
        raise ValueError("separator cannot be empty")

    separator_index = find_first_separator(input, separator)

    if separator_index == -1:
        return [input]

    token = copy_text(input, 0, separator_index)
    next_input_start = separator_index + len(separator)
    remaining_input = copy_text(input, next_input_start, len(input))

    return [token] + tokenize(remaining_input, separator)


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
