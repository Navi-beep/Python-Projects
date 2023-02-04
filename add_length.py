#What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

#Example(Input --> Output)

#"apple ban" --> ["apple 5", "ban 3"]


def words(string):
    print(type(string))
    new_list = []
    for item in string:
        new_list.append(item)
        new_list.append(len(item))
    
    return new_list 


print(words(['cats', 'noodles']))


def add_length(str):
    strang = str.split()
    new_list2 = []
    for item in strang:
        new_list2.extend([item, len(item)])
        
        
    return new_list2


print(add_length('cats, birds'))



def thing(str_two):
    str_three = str_two.split()
    new_listy = []
    for s in str_three:
        new_listy.append(s)
        new_listy.append(len(s))
    return new_listy


print(thing('cats, pigeons'))