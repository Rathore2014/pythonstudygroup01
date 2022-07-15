'''list'''
users = ['administrator','ServerAdmin','NetworkAdmin','Readonly']
users.pop()
users.pop()
print(users)
'''dic'''
users = {'u1':'administrator','u2':'ServerAdmin','u3':'NetworkAdmin'}
del users['u1']
del users['u2']
print(users)