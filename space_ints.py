#Given a string of space separated integers
#Return the highest and lowest as a space separated string "-5 83"
#bonus challenge: do so for strings of numbers with random extra whitespace
#Example:
#Input: "32 27 83 25 5 -5 0 32"
#Output: "-5 83"

#Bonus Example:
#Input: "     82  1 0  -5 32  7  14  22   "
#Output: "-5 82"

def spaced_int(string):
    thing = string.split()
    return '"{}"'.format(min(thing) + ' ' + '{}'.format(max(thing)))




print(spaced_int("32 27 83 25 5 -5 0 32"))
print(spaced_int("32 99 83 25 -15 -5 0 32"))