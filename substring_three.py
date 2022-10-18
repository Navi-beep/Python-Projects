#A string is good if there are no repeated characters.

#Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

#Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

#A substring is a contiguous sequence of characters in a string.


#Example 1:

#Input: s = "xyzzaz"
#Output: 1
#Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
#The only good substring of length 3 is "xyz".

def countGoodSubstrings(s):
        counter = 0
        for i in range(len(s)):
            #making the string into a set, removes the duplicates, so if there are 3 in a set, it means its unique as there are no duplicates within the set. 
            if len(set(s[i:i+3])) == 3:
                counter += 1
        return counter

print(countGoodSubstrings('xyzzaz'))