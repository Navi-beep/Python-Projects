from collections import Counter

#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

#There is only one repeated number in nums, return this repeated number.

#You must solve the problem without modifying the array nums and uses only constant extra space.

 

#Example 1:

#Input: nums = [1,3,4,2,2]
#Output: 2

def find_dup(nums):
    a = Counter(nums)
    for k,v in a.items():
        if v >= 2:
            return k




print(find_dup([1,2,2,3,4]))