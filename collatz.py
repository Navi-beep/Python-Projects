


def collatz(n):
    #n = 1
    while n > 1:
        print(n)
        n += 1
        if n == 1001:
            break


print(collatz(2))

#returning nothing?
def cats(c):
    #count = 0 
    while c != 1:
        if c % 2 == 0:
            c = c // 2
            #count +=1
        else:
            c = 3*c+1
            #count +=1
    
    else:
        return c
        

print(cats(3))