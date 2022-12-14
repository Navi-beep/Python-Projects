#Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.



#have to change to include spaces 

def to_weird_case(words):
    words2 = ''
    #print(len(words))
    for i in range(len(words)):
        if i % 2 == 0:
            words2 += words[i].upper()
             

        elif i % 2 == 0 or words[i] == 0:
           b = words[i].upper()
           words2 += b


        else:
            words2 += words[i].lower()


    return words2


def second_weird_case(words):
    counter = 0 
    words3 = ''
    
    for i in range(len(words)):
        if words[i] == ' ':
            counter = -1 
            words3 += words[i]

        elif counter % 2 == 0:
            words3 += words[i].upper()

        else:
            words3 += words[i].lower()
        
        counter += 1

    return words3


print(second_weird_case('this is a test'))
#print(range(len('this is a test')))


def second_to_weird_case(words):
    index = 0
    new_string = ''
    for word in words:
        if word == ' ':
            index = -1
            new_string += word
        elif index % 2 == 0:
            new_string += word.upper()
        else:
            new_string += word.lower()
        index += 1
    return new_string

print(second_to_weird_case('this is a test'))

