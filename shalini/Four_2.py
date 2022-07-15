users = {'u1':'administrator','u2':'ServerAdmin','u3':'NetworkAdmin'}
key = input("Please enter a key :")
if key in users:
    print(f"Key match succesfully{key}")
else:
    print(f"{key} match unsuccesfully")