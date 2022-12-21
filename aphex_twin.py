def aphex_twin():
    fav_songs = []

    song_name = input(f"What's your favorite Aphex Twin song?: ")
    
    res = input(f"{song_name} is a great song! Do you want me to add to your favorite songs list? Select 'y' or 'n' ")

    if res == 'y':
        print("Ok! I'll add it your favorite list")
        fav_songs.append(song_name)

    if res == 'n':
        print(" I won't add it to your favorite songs list!")
        res2 = (f"would you like to see your current favorite songs? select 'y' or 'n'")

        if res2 == 'y':
                print(fav_songs)

    else:
        print(fav_songs)
    




aphex_twin()