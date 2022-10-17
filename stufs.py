#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

#Each letter in magazine can only be used once in ransomNote.

#Example 1:

#Input: ransomNote = "a", magazine = "b"
#Output: false



def canConstruct(ransomNote, magazine):
    for r in set(ransomNote):
        # use .count to return the number of times an object appears in a list. 

        if magazine.count(r) < ransomNote.count(r):
            return False
        # if the count of r in magazine is less than the count of r in ransomNote, return False, as are r appears LESS times in magazine, than in ransomNote. therefore, a ransomNote cannot have more r than present in magazine. 
            
    return True


print(canConstruct('aa', 'ab'))