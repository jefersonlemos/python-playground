def is_separator_at(input, separator, index):
    if index + len(separator) > len(input):
        return False

    for separator_index in range(len(separator)):
        if input[index + separator_index] != separator[separator_index]:
            return False

    return True


def tokenize(input, separator):
    if separator == "":
        raise ValueError("separator cannot be empty")

    tokens = []
    current_token = ""
    index = 0

    while index < len(input):
        if is_separator_at(input, separator, index):
            tokens.append(current_token)
            current_token = ""
            index += len(separator)
        else:
            current_token += input[index]
            index += 1

    tokens.append(current_token)
    return tokens


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
