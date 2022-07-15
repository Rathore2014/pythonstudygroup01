users = ['administrator','ServerAdmin','NetworkAdmin']
print(f"user {users[2]} is not valid anymore")
users[2] = "ReadOnly"
print(f"valid users are {users[0]},{users[1]},{users[2]}")
'''dict'''
users = {'u1':'administrator','u2':'ServerAdmin','u3':'NetworkAdmin'}
print(f"user {users['u3']} is not valid anymore")
users[2] = "ReadOnly"
print(f"valid users are {users['u1']},{users['u2']},{users['u3']}")