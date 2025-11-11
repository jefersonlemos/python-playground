word = "hello"
drow = ""
position = 1
max_sequence = len(word)
iterzim = iter(word)
words_indexes = {}

while position <= max_sequence:
    
    words_indexes = {
        f"position_{position}": next(iterzim)
    }
    position += 1

print(words_indexes)
















