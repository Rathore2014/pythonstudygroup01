spp_size1 = input("Enter first spp size")
spp_size2 = input("Enter second spp size")
spp_size3 = input("Enter third spp size")
if spp_size1 > spp_size2:
     print("The max sppsize is{spp_size1}")
elif spp_size1 == spp_size2:
    print("Both spp size equal ")
else:
    print(f"The max spp size {spp_size2}")
if spp_size1 < spp_size3:
    print("The max spp size {spp_size3}")
elif spp_size2 == spp_size3:
    print(f"The max size is {spp_size2}{spp_size3}")
else:
   print(f"The max size is {spp_size1}")
if  spp_size2 > spp_size3:
    print(f"The max size is {spp_size2}")
elif  spp_size2 < spp_size3:
    print(f"The max size is {spp_size3}")
else:
     print(f"The max spp size is{spp_size1}")