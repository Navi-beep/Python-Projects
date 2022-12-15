import random 

movies = ['zoolander 2', 'harold and kumar go to white castle', 'inglorious basterds','step brothers', 'bruno', 'shaun of the dead','the dictator', 'la bamba', 'family guy', 'king of the hill']


def pick_one(movies):
    print('          ')
    print('Your movie choice for the evening is:        \n')
    print(random.choice(movies).title())
    print('          ')
    


pick_one(movies)