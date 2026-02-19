Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list[]

a=[3,4.5,"python",6+9j,True,False]
print(a)
[3, 4.5, 'python', (6+9j), True, False]

type(a)
<class 'list'>
b=6
type(b)
<class 'int'>
c=[6]
type[c]
type[[6]]
type(c)
<class 'list'>


#append
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)

a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]

#extend
a.extend("html","css")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.extend("html","css")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["html","css"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai'], 'html', 'css']




#insert()

a=["apple","banana","mango"]
a.insert(1,"ornage")
a
['apple', 'ornage', 'banana', 'mango']

a=["cyber","hacking","malware"]
a.insert(3,"linux")
a
['cyber', 'hacking', 'malware', 'linux']


#index()
a=["black","white","blue","red","green"]
a.index("blue")
2


#copy()

a.copy()
['black', 'white', 'blue', 'red', 'green']
b=a.copy()
b
['black', 'white', 'blue', 'red', 'green']
a
['black', 'white', 'blue', 'red', 'green']



#sort()
a=["briyani","icecream","chocolate","pizza"]
a.sort(0
       a
       
SyntaxError: incomplete input
a.sort()
       

a
       
['briyani', 'chocolate', 'icecream', 'pizza']

b=[2,6,1,7,9,4]
       
a.sort()
       
a
       
['briyani', 'chocolate', 'icecream', 'pizza']
b
       
[2, 6, 1, 7, 9, 4]


c=[-12,0,-3,-9,-6,-2]
       
c.sort()
       
c
       
[-12, -9, -6, -3, -2, 0]


#reverse()
       
a=["ai","cyber","ml","python","ds"]
       
a.reverse()
       
a
       
['ds', 'python', 'ml', 'cyber', 'ai']

b=[6,9,5,3,2,7]
       
b.reverse()
       
b
       
[7, 2, 3, 5, 9, 6]


#pop()
       
a=["html","cyber","css","js"]
       
a.pop()
       
'js'
a
       
['html', 'cyber', 'css']
a.pop("css")
       
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.pop("css")
TypeError: 'str' object cannot be interpreted as an integer

a.pop(1)
       
'cyber'
a.pop(0)
       
'html'

a.append()
       
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.append()
TypeError: list.append() takes exactly one argument (0 given)
a

a.append("cyber")
       
a
       
['css', 'cyber']
a.append("html")
       
a
       
['css', 'cyber', 'html']




#remove()
       
a=["hii","hello","students"]
       
a.remove("hii")
       
a
       
['hello', 'students']


#len()
       

a="code"
       
len(a)
       
4
b=["code"]
       
len(b)
       
1

c=["cyber","security"]
       
len(c)
       
2


#count()
       

a=["sun","sky","star","moon"]
       
a.count("star")
       
1

a=["water","fire","water","air"]
       
a.count("water")
       
2


#clear()
       

a=["water","drink","cool"]
       
a.clear()
       
a
       
[]
b=[]
       
b.append("juice")
       
b
       
['juice']



a=[9,1,5,2,8,4,6,3,7,0]
       
#[7,6,4,3,0,9,8,5,2,1]
       

a.sort()
       
a
       
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
       
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a=[9,1,5,2,8]
       
b=[4,6,3,7,0]
       
a.sort()
       

a
       
[1, 2, 5, 8, 9]
b.sort()
       
>>> 
>>> b
...        
[0, 3, 4, 6, 7]
>>> b.reverse()
...        
>>> 
>>> b
...        
[7, 6, 4, 3, 0]
>>> a.reverse()
...        
>>> a
...        
[9, 8, 5, 2, 1]
>>> print(b+a)
...        
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #tuple()
...        
>>> 
>>> a=(3,6.7,"hello",5+6j,True,False)
...        
>>> print(a)
...        
(3, 6.7, 'hello', (5+6j), True, False)
>>> type(a)
...        
<class 'tuple'>
>>> 
>>> a.index("hello")
...        
2
>>> len(a)
...        
6
>>> a.count(True)
...        
1
>>> 
>>> 
