word = "hello"
drow = ""
word_len = len(word)
i = 0

while i < word_len:
    last_letter = word_len
    drow += word[last_letter - i - 1]
    i += 1

print(drow)

