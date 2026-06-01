def is_separator(input, separator, index):
    separator_index = 0

    while separator_index < len(separator):
        input_index = index + separator_index

        if input_index >= len(input):
            return False
        if input[input_index] != separator[separator_index]:
            return False

        separator_index += 1

    return True


def copy_range(input, start_index, end_index):
    text = ""
    index = start_index

    while index < end_index:
        text += input[index]
        index += 1

    return text


def get_token_ranges(input, separator):
    token_ranges = []
    token_start = 0
    index = 0

    while index < len(input):
        if is_separator(input, separator, index):
            token_ranges.append([token_start, index])
            index += len(separator)
            token_start = index
        else:
            index += 1

    token_ranges.append([token_start, len(input)])
    return token_ranges


def tokens(input, token_ranges):
    tokens = []
    range_index = 0

    while range_index < len(token_ranges):
        token_start = token_ranges[range_index][0]
        token_end = token_ranges[range_index][1]
        tokens.append(copy_range(input, token_start, token_end))
        range_index += 1

    return tokens


def tokenize(input, separator):
    if separator == "":
        raise ValueError("separator cannot be empty")

    token_ranges = get_token_ranges(input, separator)
    return tokens(input, token_ranges)


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
