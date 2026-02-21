Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dict part2

#get()

a={"name":"pooja","city":"vij","mailid":"mahesh2@gmail.com"}
a.get("name")
'pooja'

#copy()
a.copy()
{'name': 'pooja', 'city': 'vij', 'mailid': 'mahesh2@gmail.com'}

#clear()
a.clear()
a
{}
b={}
b.update{"mobileno":123456789}
SyntaxError: invalid syntax
b.update{("mobileno":123456789)}
SyntaxError: invalid syntax
>>> 
>>> 
>>> a={"name":"mahesh","year":2026,"month":2,"name":"mahesh"}
>>> print(a)
{'name': 'mahesh', 'year': 2026, 'month': 2}
>>> 
>>> a
{'name': 'mahesh', 'year': 2026, 'month': 2}
>>> a={"name":"mahesh","year":2026,"month":2,"name1":"mahesh"}
>>> 
>>> print(a)
{'name': 'mahesh', 'year': 2026, 'month': 2, 'name1': 'mahesh'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a={"idnos":[10,20,30],"name":["mahesh","surya","jagadeesh"],"place":["vij","ban","hyd"]}
>>> print(a)
{'idnos': [10, 20, 30], 'name': ['mahesh', 'surya', 'jagadeesh'], 'place': ['vij', 'ban', 'hyd']}
>>> a.keys()
dict_keys(['idnos', 'name', 'place'])
>>> 
>>> a.value()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
>>> a.values()
dict_values([[10, 20, 30], ['mahesh', 'surya', 'jagadeesh'], ['vij', 'ban', 'hyd']])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('name', ['mahesh', 'surya', 'jagadeesh']), ('place', ['vij', 'ban', 'hyd'])])
>>> 
>>> 
