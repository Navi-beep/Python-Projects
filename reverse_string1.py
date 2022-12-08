#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

#Input: s = "hello"
#Output: "holle"

#leetcode problem answer
#Algorithm 2 - Reverse and Replace:
#The idea is to first extract all vowels from s and then reverse it. Next, replace the vowels in the original s with the extracted and reversed vowels.



def reverseVowels(s):
        vowels = {'a','A','e','E','i','I','o','O','u','U'}
        s = list(s)

        # extract all vowels from s
        vowelInS = [c for c in s if c in vowels]
        # reverse the extracted vowels
        reversedVowel = vowelInS[::-1]

        # replace the vowels in s with the reversed ones
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = reversedVowel.pop(0)

        return ''.join(s)

print(reverseVowels('hello'))