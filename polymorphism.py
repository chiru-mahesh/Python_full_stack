#polymorphism

#operator overloading


'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(6))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2))
print(a.__pow__(2))
print(a.__le__(8))
print(a.__ge__(3))

a=[1,2,3,4,5,6];b=[6,7,8,9,10,11]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(5))

a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b))
print("mahesh".__add__(" "+"g").title())'''




#task1
#square 
'''****
****
****
****


#right-angle
*
***
****
*****

#reverse-angle

*****
****
***
**
*

#pyramid

     *
    **
    ***
   ****'''



#square

'''n = 4
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()'''


#right-angle

'''n = 5
for i in range(1, n+1):
    print("*" * i)'''


#reverse-angle

'''n = 5
for i in range(n, 0, -1):
    print("*" * i)'''


#pyramid

'''n = 4
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)'''



#operator override


'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(6)
y=B(4)
#x=6
#y=4
print(x+y)'''



#method overloading

'''class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends")
x=New()
x.sum()
x.sum(3,4,5)
x.sum(6,2)'''



#Task

'''class New():
    def sum(self,a=4,b=2,c=3):
        if a==4 and b==2 and c==3:
            print("the sum is",a+b+c)
        elif a==6 and b==2:
            print("the product is",a*b)
        else:
            print("program ends")
x=New()
x.sum()
x.sum(4,2,3)
x.sum(6,2)'''


#method overriding


'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("Dog can barks")

a=Animal()
b=Dog()
a.speak()
b.speak()'''




'''class vehicle():
    def bike(self):
        print("bike moves fast")
class vehicle1():
    def car(self):
        print("volvo is a car ")

a=vehicle()
b=vehicle1()
a.bike()
b.car()'''
