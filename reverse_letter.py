#Given a string str, reverse it and omit all non-alphabetic characters.


def reversed(string):
    return string[::-1] 


print(reversed('cat2s'))


def two(stringy):
    new_thing = []
    for t in stringy:
        if t.isalpha():
            new_thing.append(t)
    return ''.join(new_thing[::-1]) 


print(two('ca34ts2'))