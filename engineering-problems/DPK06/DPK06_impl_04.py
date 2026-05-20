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

def collect_next_token(input, separator, start_index):
    token = ""
    index = start_index

    while index < len(input):
        if is_separator(input, separator, index):
            return token, index + len(separator), True

        token += input[index]
        index += 1

    return token, index, False

def tokenize(input, separator):
    if separator == "":
        raise ValueError("separator cannot be empty")

    tokens = []
    index = 0

    while True:
        token, index, found_separator = collect_next_token(input, separator, index)
        tokens.append(token)

        if not found_separator:
            break
        if index == len(input):
            tokens.append("")
            break

    return tokens


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))