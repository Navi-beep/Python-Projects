def runningSum(nums):
        for i in range(1,len(nums)):
            print(nums[i])
            nums[i] += nums[i-1]
        return nums 
    

print(runningSum([1,2,3,4,5]))

#add all except first number to list, doesnt quite work
def summy_sum(numberinos):
    cheese = []
    for i in range(1,len(numberinos)):
        numberinos[i] += numberinos[i-1]
        cheese.append(numberinos[i])
    return cheese

print(summy_sum([1,2,3,4,5]))