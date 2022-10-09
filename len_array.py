#You are given an array of integers arr, return the length of the longest continuous increasing subarray.
#A continuous increasing subarray is defined as 2 or more consecutive indices such that arr[i] < arr[i+1].

#Input: arr = [1,3,5,4,7]
#Output: 3
#Explanation: The longest continuous increasing subarray is [1,3,5] with length 3.
#Even though [1,3,5,7] is an increasing subarray, it is not continuous as elements 5 and 7 are separated by element
#4.

def len_array(arr):
    first = 0
    final = 0
    #print(range(len(arr)-1))
    for i in range(len(arr)-1):
        #iterate through the index values of each int
        #print(i)
        #arr[i]
        #print(arr)
        if arr[i] > arr[i+1] and len(arr[first:i+1]) > final:
            final = len(arr[first:i+1])
            first = i+1
    return final 




#print(len_array([3,1,2]))
print(len_array([1,3,5,9,7]))
