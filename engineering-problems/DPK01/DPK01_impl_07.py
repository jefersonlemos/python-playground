word = "hello"
word_len = len(word) - 1
position = 0
reverted_position = word_len - position

def get_letter(word):
    global position
    global reverted_position
 
    if reverted_position < 0:
        return word[5:]

    word += word[reverted_position]
    reverted_position -= 1
        
    #Recursion
    return get_letter(word)


print(get_letter(word))

