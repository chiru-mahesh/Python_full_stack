'''a=10
b=15
if a<b:
    print("True")'''





'''a=3
b=8
if a!=b:
    print("True")'''

'''a=2
b=4
if a==b:
    print("True")'''



'''a=4
b=4
if a==b:
    print("equal")'''


'''a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("greater")'''


'''a=int(input("a value"))
if a>40:
    print("greater")'''




'''a="python"
if a=="python":
    print("true")'''


'''a=input("mahesh")
if a=="mahesh":
    print("valid")'''





#if-condition by using logical operators
#and,or,not

'''a=5
b=9
if a<b and b>a:
    print("less")'''



'''a=7
b=11
if a<=b and b>=a:
    print("less")'''



'''a=5
b=9
if a!=b or b==a:
    print("true")'''





'''a=20
b=30
if a<b or b>a:
    print("less")'''



'''a=50
b=60
if a<=b or b>=a:
    print("less")'''


'''a=4
b=8
if not a<b:
    print("greater")'''



'''a=4
b=8
if not a>b:
    print("true")'''






'''a=int(input("a value"))
b=int(input("b value"))
if a<b or b<a:
    print("less")'''





#if-condition by using identify operators
#is , is not


'''a=7
if type(a) is int:
    print("it is int")'''


'''a=7
if type(a) is not int:
    print("it is int")'''



'''a=5.0
if type(a) is float:
    print("it is float")'''



'''a=6+9j
if type(a) is complex:
    print("it is not complex")'''



'''a=True
if type(a) is bool:
    print("it is bool")'''



'''a=1
if type(a) is bool:
    print("it is not bool")'''




'''a=5.0
if type(a) is  not float:
    print("it is float")'''



'''a=6+9j
if type(a) is not complex:
    print("it is complex")'''




'''a=1
if type(a) is not bool:
    print("it is bool")'''



'''a="hello"
if type(a) is not str:
    print("it is str")'''



'''a="hello"
if type(a) is str:
    print("it is not str")'''



'''a=bool(input("enter a"))
if type(a) is not bool:
    print("it is bool")'''





#if-condition by using membership operators
#in , not in

'''a=[2,3,4,5,6,7,8,9,10]
if 2 in a:
    print("true")'''



'''a=[2,3,4,5,6,7,8,9,10]
if 20 in a:
    print("true")'''



'''a=[2,3,4,5,6,7,8,9,10]
if 20 not in a:
    print("true")'''





'''a=[10,20,30,40,60]
b=int(input("enter a value"))
if b in a:
    print("the value is",b)'''





#if-else by using comparision operators


'''a=6
b=8
if a<b:
    print("less")'''


'''a=6
b=8
if a>b:
    print("less")
else:
    print("true")'''



'''a=6
b=8
if a<b:
    print("less")
else:
    print("false")'''






'''a=3
b=9
if a!=b:
    print("not equal")
else:
    print("equal")'''





'''a=3
b=9
if a==b:
    print("not equal")
else:
    print("equal")'''




'''a=int(input())
b=int(input())
if a>b:
    print("greater")
else:
    print("true")'''



'''a=int(input())
b=int(input())
if a<b:
    print("less")
else:
    print("true")'''








#if-else condition by using logical operators


'''a=6
b=12
if a<b and b>a:
    print("true")
else:
    print("false")'''





'''a=3
b=7
if a!=b or a==b:
    print("equal")
else:
    print("false")'''



'''a=9
b=10
if not b>a:
    print("false")
else:
    print("true")'''



'''a=int(input())
b=int(input())
if a<b and b>a:
    print("greater")
else:
    print("lesser")'''





'''a=int(input())
b=int(input())
if a!=b or b==a:
    print("greater")
else:
    print("lesser")'''




'''a=int(input())
b=int(input())
if not a!=b:
    print("greater")
else:
    print("lesser")'''




#if-else conditions by using identify operator

'''a=4
if type(a) is int:
    print("yes")
else: 
    print("no")'''


'''a="hello"
if type(a) is int:
    print("it is int")
else:
    print("it is not int")'''



'''a=int(input())
if type(a) is int:
    print("it is int")
else:
    print("it is not int")'''



'''a=9
b=10
if not b>a:
    print("false")
else:
    print("true")'''






#if-else conditions by using membership operator

'''a={4,5,6,7,8,9}
if 5 in a:
    print("yes")
else:
    print("no")'''




'''a={4,5,6,7,8,9}
if 2 not in a:
    print("true")
else:
    print("false")'''



'''a=[4,5,6,7,8,9,10]
b=int(input("a value"))
if b in a:
      print("the value is",b)
else:
    print("false")'''




'''a=[4,5,6,7,8,9,10]
b=int(input("a value"))
if b not in a:
      print("the value is",b)
else:
    print("false")'''






#if,elif,else


'''a=8
b=12
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''





'''a=8
b=12
if a==b:
    print("less")
elif b!=a:
    print("greater")
else:
    print("true")'''




'''a=8
b=12
if a==b:
    print("less")
elif b>a:
    print("greater")
elif b<a:
    print("false")
else:
    print("true")'''




'''a=6
b=4
if a>b and b>a:
    print("true")
elif a>b or b==a:
    print("equal")
elif not a!=b:
    print("less")
else:
    print("false")'''


#membership

'''a=[4,5,6,7,8,9]
b=int(input(a))
if 10 in a:
    print("true")
elif 12 not in a:
    print("false")
elif 4 in a:
    print("yes")
else:
    print("no")'''



#identify


'''a=int(input())
if type(a) is int:
    print("yes")
elif type (a) is not a:
    print("true")
else:
    print("no")'''







    


    

    



