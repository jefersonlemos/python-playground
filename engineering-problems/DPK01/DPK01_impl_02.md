# DPK02 Revert String
Create a function that can revert a string.
```
revert("Hello") -> "olleH"
```

# Table test

1. Declare the variable `word` as a string with the value `"hello"`
2. Declare the variable `drow` as an empty string
3. Declare the variable `word_len` as an int by using the function `len()` and getting the length of word(hello)
4. Declare `i` as an `int` starting with the value of `0`
5. Start the `while` statement over the variable `word_len`. It runs until the statement is `true` based on a condition.
    * 5.1 It means that it's `true` until `i` is lower than `word_len` (condition)
    * 5.2 At the first time it runs, `i=0` and `word_len=5`
        * 5.2.1. `last_letter=5`
        * 5.2.2 Gets the character from the variable `word` at the given index
        * 5.2.3 Index is `last_letter - i -1` or `4` 
        * 5.2.4 Increments the variable `drow` with the caracter `o` from `word` at the index `4`
        * 5.2.5 Increments `i` with 1. Now `i=1`

    * 5.3 Now `i=1` and `word_len=5`

        * 5.3.1 `last_letter=5`
        * 5.3.2 Gets the character from the variable `word` at the given index
        * 5.3.3 Index is `last_letter - i -1` or `3` 
        * 5.3.4 Increments the variable `drow` with the caracter `l` from `word` at the index `4`
        * 5.3.5 Increments `i` with 1. Now `i=2`

    * 5.4 Now `i=2` and `word_len=5`
        * 5.4.1 `last_letter=5`
        * 5.4.2 Gets the character from the variable `word` at the given index
        * 5.4.3 Index is `last_letter - i -1` or `2` 
        * 5.4.4 Increments the variable `drow` with the caracter `l` from `word` at the index `4`
        * 5.4.5 Increments `i` with 1. Now `i=3`

    * 5.5 Now `i=3` and `word_len=5`
        * 5.5.1 `last_letter=5`
        * 5.5.2 Gets the character from the variable `word` at the given index
        * 5.5.3 Index is `last_letter - i -1` or `1` 
        * 5.5.4 Increments the variable `drow` with the caracter `e` from `word` at the index `4`
        * 5.5.5 Increments `i` with 1. Now `i=4`

    * 5.6 Now `i=4` and `word_len=5`     
        * 5.6.1 `last_letter=5`
        * 5.6.2 Gets the character from the variable `word` at the given index
        * 5.6.3 Index is `last_letter - i -1` or `0` 
        * 5.6.4 Increments the variable `drow` with the caracter `h` from `word` at the index `4`
        * 5.6.5 Increments `i` with 1. Now `i=5`

    * 5.7 Now `i=5` and is equal to `word_len` so the statement now is `false`
    * 5.8 While Loop ends
7. Print the variable `drow`

6. Close the program