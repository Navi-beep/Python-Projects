#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

words = ['eat', 'ate', 'tea', 'ant', 'tan',
        'bat', 'adobe', 'abode', 'listen', 'silent']

def createKey(s):
    key = ''
    for c in sorted(s):
        key += c
    return str(key)

def anagram(words):
    group = dict()
    for w in words:
        if group.get(createKey(w)) == None:
            group[createKey(w)] = [w]
        else:
            group[createKey(w)].append(w)
    return group


anagram_group = anagram(words) 

anagram_grouped_list = list()

for k, v in anagram_group.items():
    anagram_grouped_list.append(v)
print(anagram_grouped_list)

