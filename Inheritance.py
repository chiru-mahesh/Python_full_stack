#Inheritance

#single inheritance

'''class RBI():  #parent class
    cash=100000
    def available_cash(cls):
        #print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI): #child-class1
    pass
class HDFC(RBI): #child-class2
    cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''




'''class RBI():  #parent class
    cash=100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI): #child-class1
    cash=20000
    def new_cash2(cls):
        print("new cash2 is",cls.cash+RBI.cash)
class HDFC(RBI): #child-class2
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()
b=SBI()
b.available_cash()
b.new_cash2()'''



#multiple inheritance


'''class Father():
    weight=80
    def Father_weight(cls):
        print("The weight of Father is",cls.weight)
        print("The weight of Father is",Father.weight)
class Mother():
    height=175
    def Mother_height(cls):
        print("the height of mother is",cls.height)
        print("the height of mother is",Mother.height)
class Son(Father,Mother):
     dob="23-06-2000"
     def dob_Son(cls):
         print("the sons dob is",cls.dob)
a=Son()
b=Father()
c=Mother()
a.dob_Son()
b.Father_weight()
c.Mother_height()'''


#multilevel inheritance

'''class Grandparents():
    acres=100
    def Grandparents_landarces(cls):
        print("the grandparent has arces",cls.acres)
        print("the garndparents has arces",Garndparent.arces)
class Parents(Grandparents):
    house=ownhouse
    def Parents_house(cls):
        print("the parents has own house",cls.house)
        print("the parents has own house",parents.house)
class child(Parents):
    gift=car
    def child_car(cls):
        print("the child has car",cls.gift)
        print("the child has car",child.car)
a=child()
a.Grandparents_landarces()
a.parent_house()
a.child_car()'''
        
