def tokenize(input, separator):
    tokenized_input = []
    token = ""

    for char in input:
        if char != separator:
            token += char
            print(token)
            #TODO - Gotta find a way to add the last item because 
            # there's no more separator to go to the else statement
        else:
            tokenized_input.append(token)
            token = ""
    return tokenized_input

    # for each separator
    #     replace with comma
    #     append to the tokenized_input list
    


print(tokenize("My god, this is awesome.", ","))