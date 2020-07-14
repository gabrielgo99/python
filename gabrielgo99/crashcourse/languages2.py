favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'eduard': 'ruby',
    'phil': 'python',
    }
new_people = [ 'phil', 'john', 'andrew', ' mohamed', 'sarah','isabelle' ]

for people in new_people:
    if people in  favorite_languages.keys():
        print(people, "\nThanks for taking the poll")
    else:
        print(people, "\nPlease take the poll")
    
