def tokenize(input, separator):
    tokenized_input = []
    token = ""

    for char in input:
        if char != separator:
            token += char
        else:
            tokenized_input += token
            token = ""
    return tokenized_input

    # for each separator
    #     replace with comma
    #     append to the tokenized_input list
    


print(tokenize("My god, this is awesome.", ","))