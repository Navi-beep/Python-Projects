#Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

#Examples
#"hello"     -->  "hll"

def vowel_remove(thing):
    cat = []
    for t in thing:
        if t not in 'aeiou':
            cat.append(t)
    return cat 
        


print(vowel_remove('hello'))