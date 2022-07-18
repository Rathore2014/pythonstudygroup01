# 1..........Read: Write a program to prompt for a file name, and then read content of the file.

fileobj = open("marks.json","r")
content = fileobj.read()
print('"strs"')

json_data ={
    'name':'Ankita',
    'age':28
}
print(type(json_data))
print(json_data)
try:
    print(json_data['name'])
except Exception as e:
    print(e)



