#You are given an initial 2-value array (x). You will use this to calculate a score.

#If both values in (x) are numbers, the score is the sum of the two. If only one is a number, the score is that number. If neither is a number, return 'Void!'.

#Once you have your score, you must return an array of arrays. Each sub array will be the same as (x) and the number of sub arrays should be equal to the score.

#For example:

#if (x) == ['a', 3] you should return [['a', 3], ['a', 3], ['a', 3]].


def explode(arr):
    sum = 0
    new_arr = []
    for i in range(len(arr)):
        if arr[i] in range(0,9):
            sum += arr[i]
        else:


    return sum
    

    


print(explode([2,3]))