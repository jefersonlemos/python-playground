word = "hello"
drow = ""
word_len = len(word)


for position in range(word_len):
    current_letter = word_len - position - 1
    print("position", position)
    print("current_letter", current_letter)
    xunga = word[current_letter]
    print("drow", xunga)
    print("########")
    drow += word[current_letter]
    

    
print(drow)



