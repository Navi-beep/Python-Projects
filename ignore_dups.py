#Please write a function that sums a list, but ignores any duplicate items in the list.

#For instance, for the list [3, 4, 3, 6] , the function should return 10.

from collections import Counter 

def sum_41(l):
    counts = dict(Counter(l))
    sum = 0
    for key, value in counts.items():
        if value < 2:
            sum += key
            #print(key)
    return sum  


    


print(sum_41([3,4,3,6]))


