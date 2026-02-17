Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#operator

#Arithmetic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a/b)
0.5
print(a**b)
16
print(a//b)
0



#Assignment
a=5
a=7
a+=b
a
11
a-=3
a
8
a*=2
a
16
a/=3
a
5.333333333333333
a//=3
a
1.0


#Assignment2
a=2
b=6
a+=b
b
6
b-=3
b
3
b*=2
b
6
b/=7
b
0.8571428571428571
b//=4
b
0.0
b**=4
b
0.0
b%=2
b
0.0




#comparsion

a=5
b=9
a<b
True
a>b
False
a>=b
False
a<=b
True
a==b
False
a!=b
True



#Logical

a=6
b=12
a<b and a>b
False
a>b and b<a
False
a<=b and b>=a
True
a!=b and a==b
False

a<=b or b<a
True
a>=b or b<=a
False
a<=b or a==b
True

not True
False
note False
SyntaxError: incomplete input
not False
True



#Identify

a=4
if type(a) is int:
    print("it is int")

    
it is int


if type(a) is not int:
    print("its not")

    

#Membership
    

a=3,4,5,6,7,8,9,10
if 10 in a:
    print(10)

    
10
>>> 
>>> if 20 in a:
...     print(20)
... 
...     
>>> 
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> 
>>> 
>>> 
>>> #Bitwise
>>> 
>>> a=4
>>> a>>3
0
>>> 
>>> a=8
>>> a<<3
64
>>> 
>>> a=3
>>> a<<4
48
>>> 
>>> a=2
>>> b=4
>>> a
2
>>> 
>>> a|b
6
>>> 
>>> a=3
>>> b=4
>>> a&b
0
>>> 
>>> a=6
>>> b=5
>>> a^b
3
>>> 
