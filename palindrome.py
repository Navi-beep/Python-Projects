#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward.

#For example, 121 is a palindrome while 123 is not.

def palindrome(x):
    if x < 0:
        return False
    new_int = (str(x)[::-1])
    if int(new_int) == x:
        return True
    else:
        return False

print(palindrome(-565))