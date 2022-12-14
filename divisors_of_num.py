#Count the number of divisors of a positive integer n.

#Random tests go up to n = 500000.

#Examples (input --> output)
#4 --> 3 (1, 2, 4)
#5 --> 2 (1, 5)

from collections import Counter

def divisors(n):
    count = 0 
    jazz = []
    for num in range(1,n+1):
        if n % num == 0:
            count += 1
            jazz.append(num)
        else:
            pass 

    return count  
    


print(divisors(4))