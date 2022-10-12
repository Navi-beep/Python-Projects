


def plus_one(nums):
    new = ''
    for n in nums:
        new += str(n)
        two_new = int(new) + 1

    return list(str(two_new))  

    


print(plus_one([1,2,3,4]))