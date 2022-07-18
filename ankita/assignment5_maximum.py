# Max number from List: WAP to find largest number from list.
#               Given list with values items = [10, 20, 30, 40, 50]


Items = [10,20,30,40,50]
largest_no = Items[0]
for n in Items:
    if n > largest_no:
        largest_no = n

print(f"The largest number in Items is: {largest_no}")
