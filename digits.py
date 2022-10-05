#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.

#Input: digits = [1,2,3]
#Output: [1,2,4]
##Explanation: The array represents the integer 123.
#Incrementing by one gives 123 + 1 = 124.
#Thus, the result should be [1,2,4].

#Input: digits = [4,3,2,1]
#Output: [4,3,2,2]
#Explanation: The array represents the integer 4321.
#Incrementing by one gives 4321 + 1 = 4322.
#Thus, the result should be [4,3,2,2].

#def larger_int(items):
#    count = 0 
#    for i in items:
#        count += i
#    b = str(count + 1)
#    return list(b)

#print((larger_int([4,3,2,1])))

def larger_int(items):
    e = ''
    for i in items:
        e += str(i)
    b = int(e) + 1
    c = list(str(b))
    return c 

    

print(larger_int([4,3,2,1]))
print(larger_int([1,2,3]))