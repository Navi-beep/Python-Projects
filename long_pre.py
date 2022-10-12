#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

 

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"


def long_pre(strs):
       
        if not strs:
            return ""

        smallest = min(strs, key=len)
        for i, x in enumerate(smallest):
            for other in strs:
                if other[i] != x:
                    return smallest[:i]
        return smallest


print(long_pre(["flower","flow","flight"]))

def longest_Prefix(b):
        
        
        prefix = b[0]
        #print(prefix)
        
        for i in b:
            #print(i)
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                print(prefix)
                #print(prefix)
                
        
        return prefix

print(longest_Prefix(["catsapp","catscookie","catskibbles"]))

    
