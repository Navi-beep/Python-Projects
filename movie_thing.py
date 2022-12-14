import random 

movies = ['zoolander 2', 'harold and kumar go to white castle', 'inglorious basterds','step brothers', 'bruno', 'shaun of the dead','the dictator', 'la bamba']


def pick_one(movies):
    print('          ')
    print('Your movie choice for the evening is:        \n')
    print(random.choice(movies))
    print('          ')
    


pick_one(movies)