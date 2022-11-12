def add_info(name,address):
    
    print("Press 'q' to quit")
    
    all_deets = {}
    
    while True:
        name = input('\nWhat is their name?:')   
        if name == 'q':
            break

        address = input('\nWhere do they live?')
        if address == 'q':
            break
        
        quit = input('\nDo you want to enter more info?')
        if quit == 'no':
            
            if name not in all_deets:
                all_deets[name] = address
        
        else:
            continue
        print(all_deets)
        
    #for key,value in all_deets:
    #        print(f"{key} lives at {value}")       

add_info('name','address')