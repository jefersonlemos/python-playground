def tokenize(input, separator):
    if separator == "":
        raise ValueError("separator cannot be empty")

    tokens = []
    token = ""
    separator_part = ""
    index = 0

    while index < len(input):
        separator_index = len(separator_part)

        if input[index] == separator[separator_index]:
            separator_part += input[index]
            index += 1

            if len(separator_part) == len(separator):
                tokens.append(token)
                token = ""
                separator_part = ""
        else:
            if separator_part != "":
                token += separator_part
                separator_part = ""
            else:
                token += input[index]
                index += 1

    token += separator_part
    tokens.append(token)

    return tokens


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
