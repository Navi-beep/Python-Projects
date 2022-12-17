#Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

#The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

def sum_arry(arr):
    max_value = max(arr)
    #print(max_value)
    min_value = min(arr)
    #print(min_value)
    return sum(arr) - max_value - min_value

print(sum_arry((1,2,3,4,5,6,10)))


def sum2_array(arry):
    return sum(arry)

print(sum2_array([]))