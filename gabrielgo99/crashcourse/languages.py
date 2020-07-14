favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'eduard': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is ",
    favorite_languages['sarah'].title())

for name, language in favorite_languages.items():
    print(name.title(), "favorite language is ", language.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print("  Hi ", name.title(), 
            ", I see your favorite language is ",
            favorite_languages[name].title(), "!")

for name in sorted(favorite_languages.keys()):
    print(name.title()," thank you for taking the poll.")

for language in set(favorite_languages.values()):
    print(language.title())

