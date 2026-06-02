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


def create_parts(input, separator):
    parts = []
    index = 0

    while index < len(input):
        if is_separator(input, separator, index):
            parts.append(None)
            index += len(separator)
        else:
            parts.append(input[index])
            index += 1

    return parts


def create_tokens(parts):
    tokens = []
    token = ""
    index = 0

    while index < len(parts):
        if parts[index] is None:
            tokens.append(token)
            token = ""
        else:
            token += parts[index]

        index += 1

    tokens.append(token)
    return tokens


def tokenize(input, separator):
    if separator == "":
        raise ValueError("separator cannot be empty")

    parts = create_parts(input, separator)
    return create_tokens(parts)


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
