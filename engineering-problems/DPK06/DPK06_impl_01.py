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
            tokenized_input.append(token)
            token = ""
    return tokenized_input

    # for each separator
    #     replace with comma
    #     append to the tokenized_input list
    


print(tokenize("My god, this is awesome.", ","))