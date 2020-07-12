rivers = {
    'nile' : 'egypt',
    'ebro' : 'spain',
    'missisypy' : 'usa',
    }
for river, country in  rivers.items():
    print ("The", river.title(), "runs through", country.title())
for river in rivers.keys():
    print(river.title())
for river in rivers.values():
    print(river.title())
