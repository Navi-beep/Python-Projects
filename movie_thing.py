import random 

movies = ['zoolander 2', 'harold and kumar go to white castle', 'inglorious basterds']


def pick_one(movies):
    return random.choice(movies);


print(pick_one(movies))