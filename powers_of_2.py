def powers_of_two(n):
    cats = []
    for c in range(n+1):
        cats.append(2**c)   
    return cats


print(powers_of_two(4))


