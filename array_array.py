#You are given an initial 2-value array (x). You will use this to calculate a score.

#If both values in (x) are numbers, the score is the sum of the two. If only one is a number, the score is that number. If neither is a number, return 'Void!'.

#Once you have your score, you must return an array of arrays. Each sub array will be the same as (x) and the number of sub arrays should be equal to the score.

#For example:

#if (x) == ['a', 3] you should return [['a', 3], ['a', 3], ['a', 3]].

#wtf does this even do? 
def explode(arr):
    sum = 0
    new_arr = []
    for n in arr:
        if n in range(0,9):
            sum += n
            new_arr.append(n) 

        else:
          sum == 1
                
    return new_arr, sum   
    


print(explode([5]))


def calculate_score(x):
  if isinstance(x[0], int) and isinstance(x[1], int):
    score = x[0] + x[1]
  elif isinstance(x[0], int):
    score = x[0]
  elif isinstance(x[1], int):
    score = x[1]
  else:
    return 'Void!'

  return [x] * score


print(calculate_score([5,3]))