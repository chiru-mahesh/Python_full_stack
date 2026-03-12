#keyword and positional argument


'''def Details(id,name,mailid):
    id=10
    name="mahesh"
    mailid="mahesh02@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''




'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="surya",mailid="s@gmail.com")
Details(id=30,name="naveen",mailid="n@gmail.com")
Details(40,"ajay","a@gmail.com")
Details("krishna","k@gmail.com",50)
Details(name="adhitya",mailid="n@gmail.com",id=30)'''




#default arguments

'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",50)'''    




'''def Grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''



'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''



'''def Grocery(item="ghee",price):     
    print("item is %s" %item)       #non-def arg follows def arg
    print("price is %.2f" %price)
Grocery(500)'''




#name price quantity,


'''def cake(itemname="choco cake",price=1500,Quality="2kg"):
    print("itemname is %s" %itemname)
    print("price is %.2f" %price)
    print("Quantity is %s" %Quality)
cake()'''




'''def cake(itemname,price,Quality):
    print("itemname is %s" %itemname)
    print("price is %.2f" %price)
    print("Quantity is %s" %Quality)
cake("coolcake",1600,"4kg")'''





'''def cake(itemname,price=1500,Quality="2kg"):
    print("itemname is %s" %itemname)
    print("price is %.2f" %price)
    print("Quantity is %s" %Quality)
cake("berry cake")'''






#*argument-> * is used to unpack the elements

'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''



'''b=(2,3,4,5,6,7,8)
print(b)
print(*b)
print(type(b))'''


'''c={4,5,6,7,8,9}
print(c)
print(*c)
print(type(c))'''



'''d={"year":2026,"month":3}
print(d)
print(*d)
print(type(d))'''



'''a,b,c=2,3,4,5,6,7,8,9,10,11,12
print(a)
print(b)
print(c)'''   #error


'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''


'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''


'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''



