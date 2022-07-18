
# 3-6..........Seeing the World: Think of at least five vlans in the lab   
#              you’d like to use.
        #  Store the names in a list. Make sure the list is not in
        # alphabetical order.
        #  Print the list in its original order.
        #  Use sorted() to print your list in alphabetical order without
        # modifying the actual list.
        #  Show that your list is still in its original order by printing it.
        #  Use sorted() to print your list in reverse alphabetical order
        # without changing the order of the original list.
        #  Show that your list is still in its original order by printing it again.
        #  Use reverse() to change the order of your list. Print the list to
        # show that its order has changed.
        #  Use sort() to change your list so it’s stored in alphabetical order.
        # Print the list to show that its order has been changed.

# Using List
num = [5,1,8,3,15,21,63,12]
print(num)
print(sorted(num))
print(sorted(num, reverse=True))
print(num)
print(num.reverse())
print(num)       

# Using Tuple
nums = (5,1,8,3,15,21,63,12)
# sort() and reverse() method is not valid with Tuple.
print(nums)
print(sorted(nums))
print(sorted(nums, reverse=True))

# Using Dictionary
numb = {
    2:"1231",
    4:"3213",
    5:"1632",
    1:"4524",
    3:"2131"
}
# sort() and reverse() method is not valid with Dictionary.
print(numb)
print(sorted(numb))
print(sorted(numb, reverse=True))
