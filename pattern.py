#You a given a number N. You need to print the pattern for the given value of N.

#For N = 2 the pattern will be 
#2 2 1 1
#2 1

#For N = 3 the pattern will be 
#3 3 3 2 2 2 1 1 1
#3 3 2 2 1 1
#3 2 1

#Note: Instead of printing a new line print a "$" without quotes.

def pattern(N,S):
    if N > 0:
        return "{}".format(N)*S + pattern(N-1,S)
    else:
        return "$"
def printPat(N):
    cats=""
    for i in range(N, 0,-1):
        cats += pattern(N,i)
    print(cats)

    
    
    

print((printPat(3)))