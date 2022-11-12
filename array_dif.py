#implement a difference function, which subtracts one list from another and returns the result.

#It should remove all values from list a, which are present in list b keeping their order.


def array_dif(a,b):
    c = []
    for n in a:
        if n not in b:
            c.append(n)

    return c 
            

#only works if there are no multiples
def dif_array(a,b):
    d = set()
    for number in a:
        d.add(number)
        for number in b:
            if number in d:
                d.remove(number)
    return d 





print(array_dif([2,2,2,2,4,5,6],[2,4]))
print(dif_array([1,2,3,4,5,5,5,6,6,6,7,8],[5,6]))
