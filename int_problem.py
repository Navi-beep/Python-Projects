# create a function that returns a duplicate in an array 

def return_duplicate(arr):
    seen = set()
    for n in arr:
        if n in seen:
            return n
        else:
            seen.add(n)
    return "No Duplicates" 



print(return_duplicate([1,3,4,5,5,6,7]))