#Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#Example 1:
#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"




def reverse_string(s):

    cats = ""
    for c in s:
        cats = c + cats
    return cats
    

print(reverse_string("I have a cat, her name is Jiji"))


def reverse_string(s):

    meows = s.split(" ")
    
    meow_2 = [meow_3[::-1] for meow_3 in meows]
    
   
    return " ".join(meow_2)
    

print(reverse_string("I have a cat, her name is Jiji"))

def reverse_cats(s):
    return " ".join([cat[::-1]
    for cat in s.split(' ')])

print(reverse_cats('cats are awesome'))

