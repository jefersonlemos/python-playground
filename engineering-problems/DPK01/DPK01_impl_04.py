word = "hello"
word_len = len(word)
position = word_len - 1
temp_drow = []
drow = ""

for letter in word:
    temp_drow.append(letter)

for letter in temp_drow:
    drow = drow + temp_drow[position]
    position = position - 1
    
print(drow)








