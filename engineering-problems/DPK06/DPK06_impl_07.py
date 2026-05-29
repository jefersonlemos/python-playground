def buffer_ends_with_separator(buffer, separator):
    separator_index = len(separator) - 1
    buffer_index = len(buffer) - 1

    while separator_index >= 0:
        if buffer[buffer_index] != separator[separator_index]:
            return False

        buffer_index -= 1
        separator_index -= 1

    return True


def buffer_to_string(buffer, end_index):
    text = ""
    index = 0

    while index < end_index:
        text += buffer[index]
        index += 1

    return text


def tokenize(input, separator):

    tokens = []
    buffer = []
    index = 0

    while index < len(input):
        buffer.append(input[index])

        if buffer_ends_with_separator(buffer, separator):
            token_end = len(buffer) - len(separator)
            tokens.append(buffer_to_string(buffer, token_end))
            buffer = []

        index += 1

    tokens.append(buffer_to_string(buffer, len(buffer)))
    return tokens



if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
