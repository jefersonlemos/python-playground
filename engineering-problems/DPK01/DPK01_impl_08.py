word = "hello"
word_len = len(word)
word_list = []
drow = ""

for letter in word:
    word_list.append(letter)


for i in range(len(word_list) -1, -1, -1):
    drow += word_list[i]


print(drow)
