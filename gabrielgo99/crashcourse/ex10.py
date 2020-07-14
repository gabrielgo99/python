print("Cual es tu nombre de usuario?")
users = [ 'admin', 'root', 'gabriel', 'paulo', 'angel' ]
name = input()
if name == 'admin':
    print("Hello admin, woud you like to see a status report?")
else:
    print(f"Hello", name, "thank you for login again.")
