
#list
thislist = ["mango", "strawberry", "chocolate"]
print(thislist)

#access
print(thislist[2])

#change value of an item
thislist[2] = "peach"
print(thislist)

#loop
for y in thislist:
    print(y)

if "mango" in thislist:
    print("Yes, 'apple' is in the fruits list")

#add an item to the end of thislist
thislist.append("orange")
print(thislist)

#add an item at a specified index
thislist.insert(2, "lime")
print(thislist)

#removes a specified item
thislist.remove("strawberry")
thislist.reverse()
print(thislist)

thislist.pop()
print(thislist)

del thislist[1]
print(thislist)

#how to empty thislist
thislist.clear()
print(thislist)
