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

def tokenize(input, separator):
    if separator == "":
        raise ValueError("separator cannot be empty")

    tokens = []
    token_start = 0
    index = 0

    while index < len(input):
        if matches_separator(input, separator, index):
            tokens.append(input[token_start:index])
            index += len(separator)
            token_start = index
        else:
            index += 1

    tokens.append(input[token_start:len(input)])
    return tokens


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
