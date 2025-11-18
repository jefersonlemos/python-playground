# para as proximas

# manipular var word in place
# usar map
# recursao, uma funcao chamando a ela mesma 
# algo assim

word = "hello"
word_len = len(word) - 1
position = 0



def get_letter(arg_word, arg_position):
        
    if arg_position <= word_len:
        reverted_position = word_len - arg_position
        
        
        arg_position += 1

        #Recursion
        get_letter(arg_word, arg_position)



#Starts in the position 0
coiso = get_letter(word, position)
print(coiso)

