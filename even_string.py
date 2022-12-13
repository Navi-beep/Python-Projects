#Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.



#have to change to include spaces 

def to_weird_case(words):
    words2 = ' '
    print(len(words))
    for i in range(len(words)):
        if i % 2 == 0:
           b = words[i].upper()
           words2 += b
        elif i % 2 != 0:
            words2 += words[i]

        #elif words[i] == ' ':
        #    words2 += ' '
     
    return words2 


    



print(to_weird_case('Weird string case'))


