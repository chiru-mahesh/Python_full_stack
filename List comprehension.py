
'''List comprehension:- every list comparehension can be rewritten as a for loop but every for loop can not be rewritten in list comparehension..'''


#List comprehension

a=["codegnan","pyhton","course"]
#["CODEGNAN","PYTHON","COURSE"]


'''for i in a :
    print(i.upper(),end=" ")'''


#syntax
#a=[expr for var in collection/range]



'''b=[i.upper() for i in a]
print(b)'''



'''print([i.upper() for i in a])'''



#taks
'''a=["python","java","ml"]
#["python","JAVA","ML"]

b=[(i.title()for i in a]:
    print(b)'''


   
    
'''a=[1,2,3,5,6,8,12,13]
#

b=[i**2 for i in a]
b=[i*i for i in a]
b=[pow(i,2)for i in a]
print(b)'''






#if-usage in list comprehension
'''even number to print'''

'''a=[i for i in range(16) if i%2==0]
print(a)'''



'''a=[i for i in range(16) if i%2!=0]
print(a)'''



'''a=[i**2 for i in range(16) if i%2!=0]
print(a)'''



'''fruits=["apple","grapes","mango","banana","berry","kiwi","dragon"]
a=[i for i in fruits if "a" in i]
print(a)'''


'''a=[i for i in fruits if "a" not in i]
print(a)'''



#no-elif usage in list comprehension


#if-else usage in list comprehension


'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''




'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
c=[a[i]+b[i] for i in range(5)]
print(c)'''
   
   












