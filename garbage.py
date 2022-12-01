x = ["apple", "orange"]
y = ["apple", "orange"]
z = x 
print (x is z)
print (x is y)
print (x == y)


def do_something(cats):
    return cats[0]


print(do_something(['This is Sparta!']))