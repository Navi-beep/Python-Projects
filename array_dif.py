#implement a difference function, which subtracts one list from another and returns the result.

#It should remove all values from list a, which are present in list b keeping their order.


def array_dif(a,b):
    c = []
    for n in a:
        if n not in b:
            c.append(n)

    return c 
            






print(array_dif([2,2,2,2,4,5,6],[2,4]))
