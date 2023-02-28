

#In this kata, you need to write a function that takes a string and a letter as input and then returns the index of the second occurrence of that letter in the string. If there is no such letter in the string, then the function should return -1. If the letter occurs only once in the string, then -1 should also be returned.

#Examples:

#second_symbol('Hello world!!!','l') --> 3

def second_symbol(word, symbol):
    count = 0
    cat = [w for w in word]
    for c in range(len(cat)):
        if cat[c] == symbol:
            count += 1
            if count == 2:
                return c 
        else:
            continue
    return -1  
     



print(second_symbol('cats', 'c'))


