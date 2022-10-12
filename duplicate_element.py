#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#You must implement a solution with a linear runtime complexity and use only constant extra space.

from collections import Counter 

#Example 1:

#Input: nums = [2,2,1]
#Output: 1

def dup_element(b):
    a = Counter(b)
    print(a)
    for k,i in a.items():
        print(k,i)
        if i == 1:
            return k
            

     
         
print(dup_element([4,1,2,2,1]))