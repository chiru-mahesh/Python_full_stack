Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#operator

#arithemtic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a%b)
2
print(a**b)
16



#assignment
a=5
b=7
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
12
a-=3
a
9
a*=2
a
18
a/=3
a
6.0
a//=3
a
2.0





#assigment2
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
b**=3
b
0.0

b**=6
b
0.0
b%=2
b
0.0
b%=8
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





#logical

a=6
b=12
a<b and a>b
False
a>b and b<a
False
a<=b and b>=a
True
a!<b and a==b
SyntaxError: invalid syntax
a!=b and a==b
False
a<=b or b<a
True
a>=b or b<=a
False
a<=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True







#identify
a=4
if type(a)  is int:
    print("it is int")

    
it is int







if type(a)  is not int:
    print("its not")

    








#membership
    

a=3,4,5,6,7,8,9,10
if 10 in a :
    print(10)

    
10




if 20 in a:
    print(20)

    
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #bitwise
>>> 
>>> a=4
>>> a=4
>>> a>>3
0
>>> 
>>> 
>>> a=8
>>> a<<3
64
>>> 
>>> 
>>> a=3
>>> a<<4
48
>>> 
>>> 
>>> a=2
>>> b=4
>>> a
2
>>> a|b
6
>>> 
>>> 
>>> a=3
>>> b=4
>>> a&b
0
>>> a=6
>>> b=5
>>> a^b
3
>>> 
>>> 
