#All Star Code Challenge #18

#Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

#If no occurrences can be found, a count of 0 should be returned.

#("Hello", "o")  ==>  1
#("Hello", "l")  ==>  2
#("", "z")       ==>  0




def str_count(strng, letter):
    Counter = 0 
    thing = []
    for word in strng:
        thing.append(word)
        if word == letter:
            Counter += 1
        else:
            continue
        
    return Counter

print(str_count('hello', 'o'))