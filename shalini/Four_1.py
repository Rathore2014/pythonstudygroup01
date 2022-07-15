from cgi import print_form


spp_size1 = input("Enter first spp size")
spp_size2 = input("Enter second spp size")
if spp_size1 > spp_size2:
    print(f"max spp size is : {spp_size1}")
elif spp_size1 == spp_size2:
    print(f"Both  spp are equal") 
else:      
    print(f"max spp size is : {spp_size2} ")
