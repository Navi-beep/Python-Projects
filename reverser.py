#Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321. You should do this without converting the inputted number into a string.

def reverser(num):

    rm = 0
    while num != 0:
        #remainder of num divided by 10 is stored as d (now it contains last digit)
        d = num % 10
        #print(d)
        #d is then added to the var reversed after multiplying it by 10. Multiplying it by 10 added a new place in the rm. 
        rm = rm * 10 + d
        num //= 10

    return rm 


print(reverser(543))
