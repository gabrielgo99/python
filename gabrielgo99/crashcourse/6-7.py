people = {
    'ggp': {
        'first_name': 'gabriel',
        'last_name': 'goncalves',
        'age': '45',
        'city': 'granada'
        },

    'lhr': {
        'first_name': 'lourdes',
        'last_name': 'huertas',
        'age': '39',
        'city': 'granada'
        },
        
    'afr': {
        'first_name': 'angel',
        'last_name': 'ferras',
        'age': '45',
        'city': 'ronda'
        },
        
    }
for username, user_info in people.items():
    print("\nUsername : " + username)
    full_name = user_info['first_name']  + " " +  user_info['last_name']
    age = user_info['age']
    city = user_info['city']
    print("\tFull name: " + full_name.title())
    print("\tAge: " + user_info['age'])
    print("\tCity: " + city.title())


    
