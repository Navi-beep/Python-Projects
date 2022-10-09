#Given an array of integers nums, calculate the pivot index of this array.

#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

#If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

#Return the leftmost pivot index. If no such index exists, return -1.

 

#Example 1:

#Input: nums = [1,7,3,6,5,6]
#Output: 3
#Explanation:
#The pivot index is 3.
#Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
#Right sum = nums[4] + nums[5] = 5 + 6 = 11


def pivotIndex(nums):
	# if the list is only 1 item long, we assume that 0th index is the pivot
    if len(nums) == 1:
        return 0
	# variable to track ongoing sum of left side (start at 0)
    sum_left = 0
	# the right side sum starts as the sum of the entire list
    sum_right = sum(nums)
    print(sum_right)
    for i in range(len(nums)):
		# the right sum is the entire remainder of the list... so subtract the current potential pivot value
		# from right sum to get the new right sum for this number
        sum_right -= nums[i]
		# if the current value for everything to the left of that potential pivot == everything to the right,
		# we found it!
        if sum_left == sum_right:
            return i
		# if not, increase our left sum to include this value before moving on to our next idx
        sum_left += nums[i]
	# never found one? return -1
    return -1

print(pivotIndex([6]))
print(pivotIndex([1,2,3,4,3,2,1]))

