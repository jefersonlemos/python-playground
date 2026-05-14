def is_separator_at(input, separator, index):
    if index + len(separator) > len(input):
        return False

    for separator_index in range(len(separator)):
        if input[index + separator_index] != separator[separator_index]:
            return False

    return True
