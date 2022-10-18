#check if a number and its double exists
#given an array of intergers check if there exists two integers N and M such that N is the double of M. 

#Ex 1:
#Input: [10,2,5,3]
# output: true


def find_double(d):
    for n in d:
        for m in d:
            if m * 2 == n:
                return True  
        
    return False 


print(find_double([16,12,2,14,3]))