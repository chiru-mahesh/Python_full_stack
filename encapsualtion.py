#encapsualtion

'''combine multiple unit into single unit is called encapsualtion
1.public data
2._protected data
3.__private data'''



#public data

'''class parent():
    publicdata=10
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()'''




#_protected data


'''class parent():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)
print(obj1._protecteddata)'''





#__private data

class parent():
    __privatedata="mahesh"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()











#contact base management system

'''1
add contact

2'''
