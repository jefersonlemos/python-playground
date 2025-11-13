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
        #TODO - It's working, now I need to revert the word, it's printing in the same order
        print("before incrementing",arg_position)
        print(arg_word[arg_position])
        
        
        #Position is now incremented
        arg_position += 1
        print("after incrementing",arg_position)
    
        #Recursion
        get_letter(arg_word, arg_position)



#Starts in the position 0
get_letter(word, position)

