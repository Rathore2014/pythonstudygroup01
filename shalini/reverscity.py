'''6.2 revers city name'''
def revers(str):
    chr = ""
    rstr = ""
    for chr in str:
        rstr = chr + rstr
    return rstr 
city_name = input("enter city name : ")
r_city_name = revers(city_name)
print(f"reverse of city name is {r_city_name}")
