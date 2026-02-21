Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sets()
a={6,3.5,"mahesh",6+9j,True,False}
print(a)
{False, True, (6+9j), 3.5, 6, 'mahesh'}
type(a)
<class 'set'>
b={7,9,5,6,7,9,3}
print(b)
{3, 5, 6, 7, 9}
type(b)
<class 'set'>

a={4,5,6,7,8,9}
a.add(20)
a
{4, 5, 6, 7, 8, 9, 20}

#issubset()
a={2,3,4,5,6,7}
b={5,6,7}
b.issubset(a)
True
a.issubset(b)
False

a={4,5,6,7,8,9}
b={8,9,10,11}
b.issunset(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b.issunset(a)
AttributeError: 'set' object has no attribute 'issunset'. Did you mean: 'issubset'?
b.issubset(b)
True
b.issubset(a)
False

c={6,7,8,9,10}
d={7,8,9,4,2}
d.issubset(c)
False

#superset()
a={3,4,5,6,7,8,9}
b={2,3,4,5,6}
a.isuperset(b)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.isuperset(b)
AttributeError: 'set' object has no attribute 'isuperset'. Did you mean: 'issuperset'?
a.issuperset(b)
False
a={1,2,3,4,5,6}
b={4,5,6}
a.issuperset(b)
True


#union()
a={1,2,3,2,4,5,6}
b={4,5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection()
a={4,5,6,7,10,20}
b={10,20,30,40,50}
a.intersection(b)
{10, 20}

c={20,60,70,90,100}
d={40,20.60,80,100}
c.intersection(d)
{100}


#difference()
a={2,3,4,5,6}
b={3,4,5,6,7,8}
a.difference(b)
{2}

b.difference(a)
{8, 7}

#update()

a={10,11,12,13,14}
b={11,12,13,14,15}
a.update(b)
a
{10, 11, 12, 13, 14, 15}

b.update(a)
b
{10, 11, 12, 13, 14, 15}


#difference_update()

a={2,3,4,5,6,7,8}
b={1,5,7,9,11,13}
a.difference_update(b)
a
{2, 3, 4, 6, 8}

b.difference_update(a)
b
{1, 5, 7, 9, 11, 13}

c={5,6,7,8,9}
d={5,6,4,10,9,12}
c.difference_update(d)
c
{7, 8}


d.difference_update(c)
d
{4, 5, 6, 9, 10, 12}


#symmetric_difference()

a={3,4,5,6,7,8,9}
b={1,2,3,4,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 5, 6, 7, 10, 11}
b.symmetric_difference(a)
{1, 2, 5, 6, 7, 10, 11}


#symmetric_difference_update()

a={1,3,5,7,9,11,13}
b={2,3,4,5,6,7,8,9}
a.symmetric_difference_update(b)
a
{1, 2, 4, 6, 8, 11, 13}

b.symmetric_difference_update(a)
b
{1, 3, 5, 7, 9, 11, 13}
a
{1, 2, 4, 6, 8, 11, 13}


#intersection_update()

a={1,2,3,6,4,8}
b={1,3,6,7,5,9,10}
a.intersection_update(b)
a
{1, 3, 6}

b.intersection_update(a)
b
{1, 3, 6}

c={6,7,8,9,10}
d={1,2,3,6,7,8}
c.intersection_update(d)
c
{8, 6, 7}
d.intersection_update(c)
d
{8, 6, 7}


#pop()
a={4,5,6,7,9}
a.pop()
4

#remove()
a.remove(9)
a
{5, 6, 7}


#copy()
a={4,5,6,7,9,10}
a.copy()
{4, 5, 6, 7, 9, 10}

#clear()
a.clear()
a
set()
b=set()
b.add(60,40)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    b.add(60,40)
TypeError: set.add() takes exactly one argument (2 given)
b.add(60)
b
{60}

b.discard(60)
b
set()


#isdisjoint()

a={4,5,6,7,8}
b={5,6,7,3,2}
a.isdisjoint(b)
False


c={3,6,9}
d={2,4,6}

c.isdisjoint(d)
False

e={2,4,6}
f={1,3,9}
e.isdisjoint(f)
True


a={1,3,6,4}
a.len()
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    a.len()
AttributeError: 'set' object has no attribute 'len'
len(a)
4

#count()
a.count()
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'





#dict{}
a={"name":"mahesh","year":2026,"month":"feb"}
print(a)
{'name': 'mahesh', 'year': 2026, 'month': 'feb'}
type(a)
<class 'dict'>

b={"name","year","month"}
print(b)
{'name', 'month', 'year'}
type(b)
<class 'set'>

#keys()

a.keys()
dict_keys(['name', 'year', 'month'])

a.values()
dict_values(['mahesh', 2026, 'feb'])

a.items()
dict_items([('name', 'mahesh'), ('year', 2026), ('month', 'feb')])

#accessing()

a={"year":2026,"date":17}
a["year"]
2026

#update()

a={"name":"mahesh","city":"vij"}
a.update({"mailid":"mahesh2@gmail.com"})
a
{'name': 'mahesh', 'city': 'vij', 'mailid': 'mahesh2@gmail.com'}

a.update({"date":20},{"month":"feb"})
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    a.update({"date":20},{"month":"feb"})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"date":20,"month":"feb"})
>>> a
{'name': 'mahesh', 'city': 'vij', 'mailid': 'mahesh2@gmail.com', 'date': 20, 'month': 'feb'}
>>> 
>>> 
>>> #setdeault()
>>> 
>>> a={"time":6,"hour":1,"second":26}
>>> a.setdeault()
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    a.setdeault()
AttributeError: 'dict' object has no attribute 'setdeault'. Did you mean: 'setdefault'?
>>> a.setdefault("date":20)
SyntaxError: invalid syntax
>>> a.setdefault("date",20)
20
>>> 
>>> a
{'time': 6, 'hour': 1, 'second': 26, 'date': 20}
>>> 
>>> 
>>> #pop()
>>> 
>>> a={"colour":"black","food":"briyani"}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("colour")
'black'
>>> 
>>> #popitem()
>>> a.popitem()
('food', 'briyani')
>>> 
>>> 
>>> a
{}
>>> 
>>> a={"month":"feb","food":"briyani","colour":"black"}
>>> a.pop("month")
'feb'
a
>>> 
