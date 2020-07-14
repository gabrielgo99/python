players = ['charles', 'martina', 'michael', 'florence', 'eli' ]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])# print the names from the third item though the last item
print(players[-3:]) # print the names of the last three players

print("Here are the first three playes on my team:")
for player in players[:3]:
    print(player.title())

