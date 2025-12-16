word = "olleh"
drow = ""

length = 0
for char in word:
    length = length + 1

end_pointer = length - 1
start_pointer = 0

while end_pointer >= start_pointer:
    drow = drow + word[end_pointer]
    end_pointer = end_pointer - 1

print(drow)