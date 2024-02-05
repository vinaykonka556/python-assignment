#strip()

district_name = input("enter the district name ")
list = ["viziangaram","Visakhapatnam","Srikakulam","Guntur"]

if district_name in list:
    print("yes is availble")
else:
    print(list,"not avaliable")



food = input("enter the type of biryani name ")
items = ["Hyderabadi Biryani","Chicken Dum Biryani","spy Chicken Biryani","fry picec briyani"]

if food in items:
    print("yes it available")
else:
    print(items,"not available")

    
#lstrip()
    

friuts_name = ",,..banana,apple,orange,kiwi"

a = friuts_name.lstrip(",.")

print(a)


drinks = "....,,as, sprite,string,pepsi,thums up,pulpy orange"

a = drinks.lstrip(".,as")

print(a)


#rstrip()


drinks = "sprite,pulpy orange,pepsi,,apl"

a = drinks.rstrip("., apl")

print(a)


drinks = "   sprite , pepsi...  "

a = drinks.rstrip(". ")

print(a)