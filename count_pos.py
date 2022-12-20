#Given an array of integers.

#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

#If the input is an empty array or is null, return an empty array.



def count_positives_sum_negatives(arr):
    neg_sum = 0 
    count_pos = 0
    
    for a in arr:
        
        if a > 0: 
            count_pos += 1
        
        else:
            neg_sum += a

    
    return [count_pos , neg_sum]