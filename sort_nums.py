#Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

#For example:

#solution([1,2,3,10,5]) # should return [1,2,3,5,10]
#solution(None) # should return []

#doesnt work so far
def solution(nums):
        nums_2 = list(nums)
        
        if len(nums_2) == 0:
            return nums_2
        else:
            nums_3 = sorted(nums_2)
            return nums_3
        


print(solution([1,2,3,7,6,8]))