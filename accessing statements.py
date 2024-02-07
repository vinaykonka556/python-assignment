#Accessing 40,50in below statement
list=[10,20,[30,40],50,60]
print(list[2])
print(list[2][1],list[3])

#Count()
l=[10,20,30,40,50,20,10,40]
print(l.count(10))
print(l.count(20))
print(l.count(50))

#Index()
l=[10,20,30,40,50,60]
print(l.index(20))
print(len(l))

#append()
l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append('vinaykumar')
print(l)

list=["vinaykumar","konka","Name","Python"]
list.append("vinay")
list.append("kumar")
print(list)

#insert()
l=[10,20,30,40,50,60]
l.insert(0,5)
l.insert(5,80)
print(l)

list=[10,40,"vinaykumar",50,60,"konka"]
list.insert(2,30)
list.insert(6,70)
print(list)


#extend()
list1=["apple","Berry","orange","banana"]
list2=["Kiwi","papaya","water melon"]
list1.extend(list2)
print(list1)

l1=["Maruthi","VolksWagen","Tata"]
l2=["hundai","Mahindra"]
l1.extend(l2)
print(l1)
l1.extend("BMW")
print(l1)

#remove()
list=[10,40,"vinaykumar",50,60,"konka"]
list.remove("vinaykumar")
print(list)

l=[10,20,20,30,40,50,60]
l.remove(20)
print(l)


#pop()
l=[10,20,30,40,50,60]
print(l.pop(3))

l=[10,20,30,40,50,60]
print(l.pop())