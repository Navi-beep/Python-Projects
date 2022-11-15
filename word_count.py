cats = 'i love cats'

print(cats.upper())

print('cheese kind of smell like cheese'.count('cheese'))

#count number of words in a given string
print('this is a string of cheese look at how marvelous it is.'.count(' ') + 1)

line = input()
word_total = line.count(' ') + 1 
print(word_total)


def count_words(string):
    count = 0
    new_string = string.split()
    for s in new_string:
        count += 1
    return count

    

    



print(count_words('cats are cool'))