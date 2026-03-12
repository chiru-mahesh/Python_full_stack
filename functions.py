
#functions:
#a function is a block of  organized, reuasble code that is used to perform a single or multiple task.
#python gives in build function like print, you can make your own function also and this are called user define functions.
#function blocks begin with the keyword def() followed by the function name and paranthesis () [].


'''a=10
b=20
print("the sum is",a+b)
print("the dif is",a-b)
print("the product is",a*b)


a=100
b=200
print("the sum is",a+b)
print("the dif is",a-b)
print("the product is",a*b)


a=1000
b=2000
print("the sum is",a+b)
print("the dif is",a-b)
print("the product is",a*b)'''




#functions

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the dif is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''


'''def calculate(a,b):
    print("the power is",a**b)
    print("the modules is",a%b)
    print("the remanider is",a//b)
calculate(10,20)
calculate(5,6)'''



'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
add()'''


'''def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()'''



#diff between print and return
#print just shows the human user ouptut in a console.
#return is used to terminate the function and gives back a value form the function..

#print v/s return


'''def mul(a,b):
    print(a*b)
mul(3,4)'''


'''def mul(a,b):
    return a*b
print(mul(2,3))'''


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(3,4)'''    
  


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(2,4))'''



#Task-1


'''def cal():
    a=int(input("enter the value a"))
    b=int(input("enter the value b"))
    option=int(input("enter the option"))
    if option==1:
        return a+b
    if option==2:
        return a-b
    if option==3:
        return a*b
print(cal()) '''




'''def cal():
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input("choosethe option
                           1.add
                            2.sub
                            3.mul"))'''







'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input("choosethe option
                           1.add
                            2.sub
                            3.mul"))

    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()'''



#Task-2


#split bill in functions
#by doing norml, fstring,format
#10 mem
#perhead =1000rs




'''def split_bill():
    members = 10
    per_head = 1000
    total = members * per_head

    print("Members:", members)
    print("Per Head Amount:", per_head)
    print("Total Bill:", total)
    
split_bill()'''



'''def split_bill():
    members = 10
    per_head = 1000
    total = members * per_head

    print(f"Members: {members}")
    print(f"Per Head Amount: {per_head}")
    print(f"Total Bill: {total}")

split_bill()'''





'''def splitbill():
    a=int(input("enter the total no. of friends"))
    b=int(input("enter the amount"))
    print("the bill is",b//a)
    
splitbill()'''



'''def splitbill():
    a=int(input("enter the total no. of friends"))
    b=int(input("enter the amount"))
    c=b//a
    print("perhead bill is {}".format(c))
    print(f"the bill is {c}")
    
splitbill()'''





'''def splitbill():
    a=int(input("enter the total no. of friends"))
    b=int(input("enter the amount"))
    print("perhead bill is {}".format(b//a))
    print(f"the bill is {b//a}")
    
splitbill()'''






    







    
        
    

    
