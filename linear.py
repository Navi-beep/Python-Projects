#enumerate - 

def linear_search(haystack, needle):
    for position, item in enumerate(haystack):
        if item == needle:
            return position
    return -1


print(linear_search([1,2,3,4,5,6,7,8,9,10], 8))