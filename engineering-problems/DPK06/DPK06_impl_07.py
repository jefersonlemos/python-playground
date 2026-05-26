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


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
