#Given a word (w) and some text (t), find whether w is in t. 
# For example: w="nest", t="I built a nest and tested it."

def find_word(words, word):

    new_list = words.split()

    for w in new_list:
        if w == word:
            return True

        
    return False


print(find_word('I built a nest and tested it', 'cat'))