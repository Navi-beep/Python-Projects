#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#If target is not found in the array, return [-1, -1].




def start(nums, t):
    if t not in nums:
        return [-1,-1]

    s = nums.index(t)
    e = s
    o = [s, e]
    while nums[e + 1] == t:
        e += 1
        o[1] = e

    return o 



print(start([1,2,3,4,5,6,7,8,8,9], 8))
print(start([5,7,7,8,8,10], 8))

