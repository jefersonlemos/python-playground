# DPK02 Revert String
Create a function that can revert a string.
```
revert("Hello") -> "olleH"
```

Time spent: 1 hour

# References

* https://www.w3schools.com/python/python_lists_access.asp


# Table test


1. Declare the variable `word` as a string with the value `"hello"`
2. Declare the variable `word_len` as an int by using the function `len()` and getting the length of word(hello)
3. Declare the variable `position` as an int and equals `word_len - 1`
4. Declare the variable `temp_drow` as an empty list 
5. Declare the variable `drow` as an empty string
6. Start a for loop over `word`
    * Letter equals `h`
        * Append `h` to `temp_drow` in the position `0`
    * Letter equals `e`
        * Append `e` to `temp_drow` in the position `1`
    * Letter equals `l`
        * Append `l` to `temp_drow` in the position `2`
    * Letter equals `l`
        * Append `l` to `temp_drow` in the position `3`
    * Letter equals `o`
        * Append `o` to `temp_drow` in the position `4`

7. Start a loop over the list `temp_drow`
    * concatenate `drow` with `drow` + `temp_drow` at the position `4`(o)
    * subtract `position` with `position` minus 1, (4)
    * concatenate `drow` with `drow` + `temp_drow` at the position `3`(l)
    * subtract `position` with `position` minus 1, (3)
    * concatenate `drow` with `drow` + `temp_drow` at the position `2`(l)
    * subtract `position` with `position` minus 1, (2)
    * concatenate `drow` with `drow` + `temp_drow` at the position `1`(e)
    * subtract `position` with `position` minus 1, (1)
    * concatenate `drow` with `drow` + `temp_drow` at the position `0`(h)
    * subtract `position` with `position` minus 1, (0)

8. Print the string `drow`    
    