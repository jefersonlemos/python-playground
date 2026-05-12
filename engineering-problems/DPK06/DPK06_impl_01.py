def tokenize(input, separator):
    tokenized_input = []
    token = ""
    index = 0

    while index < len(input):
        found_separator = True

        for separator_index in range(len(separator)):
            input_index = index + separator_index

            if input_index >= len(input) or input[input_index] != separator[separator_index]:
                print("len-input: ", len(input))
                print("input[input-index]: ",input[input_index])
                found_separator = False
                break

        if found_separator:
            tokenized_input.append(token)
            token = ""
            index += len(separator)
        else:
            # Each character is added to the token variable until it's complete
            token += input[index]
            index += 1

    tokenized_input.append(token)
    return tokenized_input


if __name__ == "__main__":
    print(tokenize("a,b,c,d", ","))

print(tokenize("My god, this is awesome.", ","))