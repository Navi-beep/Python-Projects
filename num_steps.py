#Given an integer num, return the number of steps to reduce it to zero.

#In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.



def even(e):
    if e % 2 == 0:
        return True

    return False


print(even(2)) 

#not working yet
def num_steps(s):
    steps = 0
    
    while s > 0:
        if s % 2 == 0:
            s = s // 2
            steps = steps + 1
            continue 
        
        else:
            s = s - 1
            steps = steps + 1
            continue
        

    return steps   

print(num_steps(2))