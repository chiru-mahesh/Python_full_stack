#oops-(Object Oriented Programming)

#oops syntax

'''class classname():
    name="codegnan"
    age=2018
    place="vija"
    def fname(method):
        print(statements.........)
a=classname()
print(dir(a))
a.fname()'''



#class declaration


'''class Details():
    name="mahesh"
    age=23
    place="vij"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''



#object instatitation

'''class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):l
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data("mahesh",23,"vij")
a.display()
b=Details()
b.Data("surya",23,"vij")
b.display()'''


#object intialization

'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
         print(self.name,self.age,self.place)
a=Details("surya",23,"vij")
a.display()
b=Details("naveen",23,"vij")
b.display()'''



#task


'''class Details():
    def __init__(self,name,age,place):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a.Details()
a.display()'''




'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
         print(self.name,self.age,self.place)
a=Details(input("name"),int(input("age")),input("place"))
a.display()'''




#difference b/w _ and __
 
'''#we generally use it for private variable, that means when ever we use double leading _ for a variable your python interpeter treats in order to avoid name conflict with method
in inter classes'''



'''class Employee():
    def __init__(self):
        self._name="mahesh"
        self._mailid="mahesh2@gmail.com"
        self.__salary=20000  #private variable
a=Employee()
print(dir(a))
print(a._name)
print(a._mailid)
#print(a.__salary)  error
print(a._Employee__salary)'''



#TASK


'''class Employee():
    def __init__(self):
        self._name="mahesh"
        self._mailid="mahesh2@gmail.com"
        self.__salary=20000
class Employee2():
    def __init__(self2):
        self2._name="surya"
        self2._mailid="surya20@gmail.com"
        self2.__salary=25000       
a=Employee()
print(dir(a))
print(a._name)
print(a._mailid)
#print(a.__salary)  error
print(a._Employee__salary)

b=Employee2()
print(dir(b))
print(b._name)
print(b._mailid)
print(b._Employee2__salary)'''




