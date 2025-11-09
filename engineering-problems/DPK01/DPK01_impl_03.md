# DPK02 Revert String
Create a function that can revert a string.
```
revert("Hello") -> "olleH"
```

# Table test

1. Declare the variable `word` as a string with the value `"hello"`
2. Declare the variable `drow` as an empty string
3. Declare the variable `word_len` as an int by using the function `len()` and getting the length of word(hello)
4. Start a for loop over a sequence of numbers using the `range` function that receives the number from the variable `word_len`
    * 4.1 First iteration - First number in range is 0
        * 4.1.1 Declares the variable `current_letter` as `word_len(5) - letter(0) - 1` which means `4`
        * 4.1.2 Increments the variable `drow` with the a letter from `word` at the position 4, which means `o`

    * 4.2 Second iteration - Second number in range is 1
        * 4.1.1 Declares the variable `current_letter` as `word_len(5) - letter(1) - 1` which means `3`
        * 4.1.2 Increments the variable `drow` with the a letter from `word` at the position 3, which means `l`

    * 4.3 Third iteration - Third number in range is 2
        * 4.1.1 Declares the variable `current_letter` as `word_len(5) - letter(2) - 1` which means `2`
        * 4.1.2 Increments the variable `drow` with the a letter from `word` at the position 2, which means `l`

    * 4.4 Fourth iteration - Fourth number in range is 3
        * 4.1.1 Declares the variable `current_letter` as `word_len(5) - letter(3) - 1` which means `1`
        * 4.1.2 Increments the variable `drow` with the a letter from `word` at the position 1, which means `e`

    * 4.5 Fifth iteration - Fifth number in range is 4
        * 4.1.1 Declares the variable `current_letter` as `word_len(5) - letter(4) - 1` which means `0`
        * 4.1.2 Increments the variable `drow` with the a letter from `word` at the position 0, which means `h`

5. Loop ends
6. Print the variable `drow`