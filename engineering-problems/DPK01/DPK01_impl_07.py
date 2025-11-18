word = "hello"
word_len = len(word) - 1


def get_letter(word):
    print("arg-word =", word)
    # print("position", position)
        
    if position <= word_len:
        reverted_position = word_len - position

        word += word[reverted_position]

        position += 1

    #Recursion
    get_letter(word)
    # return arg_word

    print("arg-pos2 =", position)
    print("arg-word2 =", word)


#Starts in the position 0


print(get_letter(word))

