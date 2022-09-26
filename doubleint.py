#Write a function that doubles every second integer in a list starting from the left.

#double_every_other([1,2,3,4]) # -> [1, 4, 3, 8]

def double_int(cats):
    for i in range(len(cats)):
        #index num
        if i % 2 == 1:
            cats[i]*= 2
    return cats

print(double_int([1,2,3,4,5,6]))

cats = [1,2,3,4,5,6]
print(range(len(cats)))


print(0 % 2)
print(1 % 2)
print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)
print(6 % 2)

#def double_ints(birds):
#    for n in range(len(birds)):
#        print(n)

#double_ints([1,2,3,4,5,6,7,8,9])

