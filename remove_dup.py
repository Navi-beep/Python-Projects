
def removeDuplicates(nums):
        replicant = 0

        for i in range(1, len(nums)):
            
            if nums[i] == nums[i - 1]:
                replicant += 1
            else:
                nums[i - replicant] = nums[i]

        return len(nums) - replicant 
        



print(removeDuplicates([1,1,2]))