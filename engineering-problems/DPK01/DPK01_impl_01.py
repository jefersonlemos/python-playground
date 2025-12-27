
word = []
drow = ""


for letter in "hello":
    word.append(letter)

word.reverse()

for letter in word:
    drow += letter

print("a palavra invertida", drow)
