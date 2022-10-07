def spin_words(sentence):
    s = sentence.split()
    q = []
    for word in s:
        if len(word) >= 5:
            q.append(word[::-1])
        else:
            q.append(word)
    return (' '.join(q))  

print(spin_words('Cats are awesome'))