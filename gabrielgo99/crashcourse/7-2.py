
prompt = ("How many people are in their dinner group?")
people = input(prompt)
peoples = int(people)
if peoples > 8:
    print("\nYou will have to wait 20 minutes for a table")
else:
    print("\nThe table is ready!")
