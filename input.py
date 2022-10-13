#Put in a character from Star Wars and get a quote! Have fun! 
#doesnt work, why is it just printing the general kenobi?
def star_wars():

    while True:
        print("Hello there! Name your favorite Star Wars character and I'll give you a quote.")
        res = input(f"What is your favorite character?: ")

        opt_1 = 'general kenobi'
        opt_2 = 'Stormtrooper'
        opt_3 = 'Yoda'
        opt_4 = 'Darth Vader'
        opt_5 = 'Han Solo'
        

        if res.lower() == opt_1.lower():
            print('Hello there General Kenobi')
                
            
        elif res.lower() == opt_2.lower():
            print("These aren't the droids you're looking for.")
                

        elif res.lower() == opt_3.lower():
            print('Fear leads to anger, anger leads to hate, hate leads to suffering')
                

        elif res.lower() == opt_4.lower():
            print('Luke, I am your father')
                

        elif res.lower() == opt_5.lower():
            print("You've never heard of the Millenium Falcon? It's the ship that made the Kessel run in less than 12 parsecs")
                
        else:
            print('You will therefore be taken to the Dune Sea, and cast into the pit of Carkoon, the nesting place of the all-powerful Sarlaac.')
            break 


star_wars()  

