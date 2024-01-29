# Print list in reverse order using a loop.
mylist =[10,"abc",20,3.6,"def"]
newlist = []
for i in range(1,len(mylist)+1):
    newlist.append(mylist[-i])
    print (newlist)