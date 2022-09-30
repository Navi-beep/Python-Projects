#Write a Python program which iterates the integers from 1 to n. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


def fizzbuzz():
    for n in range(15):
        if n % 3 == 0 and n % 5 == 0:
            print("Fizzbuzz")

        elif n % 3 == 0:
            print("Fizz")
            continue 

        elif n % 5 == 0:
            print("Buzz")
            continue
        print(n)

fizzbuzz()


class Solution:
    def fizzBuzz(self, n):
        listy = []
        for n in range(1,n+1):
            if n % 3 == 0 and n % 5 == 0:
                listy.append("FizzBuzz")
            elif n % 3 == 0:
                listy.append("Fizz")
            
            elif n % 5 == 0:
                listy.append("Buzz")
            
            else:
                listy.append(str(n)) 
        
        return listy