def iterative_factorial(n):
    factorial = 1

    for i in range(2, n + 1):
        print(i)
        factorial *= i 

    return factorial 


print(iterative_factorial(5))
