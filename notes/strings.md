# Python Strings

A string is a sequence of characters. In Python, strings are enclosed in single or double quotes.

Example:

    my_string = "Hello World!"


**String Methods:**

1. **capitalize()**: Returns a copy of the string with the first character capitalized.

Example:

    my_string = "hello world"
    print(my_string.capitalize())
    
    Output:
    Hello world

2. **upper()**: Returns a copy of the string with all characters in uppercase.

Example:

    my_string = "hello world"
    print(my_string.upper())
    
    Output:
    HELLO WORLD

3. **lower()**: Returns a copy of the string with all characters in lowercase.

Example:

    my_string = "HELLO WORLD"
    print(my_string.lower())
    
    Output:
    hello world

4. **swapcase()**: Returns a copy of the string with uppercase characters converted to lowercase and vice versa.

Example:

    my_string = "Hello World"
    print(my_string.swapcase())
    
    Output:
    hELLO wORLD

5. **replace()**: Returns a copy of the string with all occurrences of a substring replaced with another substring.

Example:

    my_string = "Hello World"
    print(my_string.replace("World", "Universe"))
    
    Output:
    Hello Universe

6. **count()**: Returns the number of occurrences of a substring in the string.

Example:

    my_string = "Hello World"
    print(my_string.count("l"))
    
    Output:
    3

7. **find()**: Returns the index of the first occurrence of a substring in the string. Returns -1 if the substring is not found.

Example:

    my_string = "Hello World"
    print(my_string.find("o"))
    
    Output:
    4

8. **index()**: Same as find() method, but raises an exception if the substring is not found.

Example:

    my_string = "Hello World"
    print(my_string.index("o"))
    
    Output:
    4

9. **isalnum()**: Returns True if all characters in the string are alphanumeric (letters or numbers).

Example:

    my_string = "Hello123"
    print(my_string.isalnum())
    
    Output:
    True

10. **isalpha()**: Returns True if all characters in the string are alphabetic (letters).

Example:

    my_string = "Hello"
    print(my_string.isalpha())
    
    Output:
    True

11. **isdigit()**: Returns True if all characters in the string are digits.

Example:

    my_string = "123"
    print(my_string.isdigit())
    
    Output:
    True

12. **isspace()**: Returns True if all characters in the string are whitespace.

Example:

    my_string = "    "
    print(my_string.isspace())
    
    Output:
    True


**String Slicing:**

Slicing is a way to extract a part of a string by specifying a range of indices. In Python, the indices start at 0 and go up to the length of the string minus one.

Example:

    my_string = "Hello World"
    print(my_string[0:5])
    
    Output:
    Hello

    In the example above, the slice [0:5] extracts the characters from index 0 up to (but not including) index 5.

Here are some other examples of slicing:

    my_string = "Hello World"
    print(my_string[:5])  # same as [0:5]
    print(my_string[6:])  # from index 6 to the end of the string

In Python, you can also use negative indices to slice strings. Negative indices count from the end of the string, with -1 being the last character, -2 being the second-to-last character, and so on.

Here are some examples of negative index slicing:

    my_string = "Hello World"  
    print(my_string[-5:-1])  # from the fifth-to-last character up to (but not including) the last character  
    print(my_string[-6:])  # from the sixth-to-last character to the end of the string  
    print(my_string[:-6])  # from the beginning of the string up to (but not including) the sixth-to-last character
    
    Output:
    Worl  
    World  
    Hello

In the first example, the slice [-5:-1] extracts the characters from the fifth-to-last character up to (but not including) the last character.

In the second example, the slice [-6:] extracts the characters from the sixth-to-last character to the end of the string.

In the third example, the slice [:-6] extracts the characters from the beginning of the string up to (but not including) the sixth-to-last character.