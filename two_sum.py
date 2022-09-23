#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# ex1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


#O(n squared) complexity

# enumerate(iterable, start=0) - Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.

#Start: the index value from which the counter is to be started, by default it is 0


def two_sum(l, t):
    p = {}

    for i, n in enumerate(l):
        diff = t - n 
        if diff in p:
            return [p[diff], i]

        p[n] = i

print(two_sum([1,2,3,4,5], 4))
