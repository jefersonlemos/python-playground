def matches_separator(input, separator, index):
    separator_index = 0

    while separator_index < len(separator):
        input_index = index + separator_index

        if input_index >= len(input):
            return False
        if input[input_index] != separator[separator_index]:
            return False

        separator_index += 1

    return True
