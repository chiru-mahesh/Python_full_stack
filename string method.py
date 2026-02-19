Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Stringmethods

#len()

a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1


#count

a="twinkle twinkle little star"

a.count("twinkle")
2

a.count("t")
5
a.count("")
28
a.count(" ")
3
a.count("l")
4


#find a string

a="code"
a.find("d")
2
a[2]
'd'

b="codegnan"
a.find("n")
-1

b.find("n")
5

a[5]+[7]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a[5]+[7]
IndexError: string index out of range
a[5]+a[7]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a[5]+a[7]
IndexError: string index out of range
b[5]+b[7]
'nn'



c="hello"
c.find("l")
2
c[2:4]
'll'


#escape sequences

#\n-> new line
#\t->tab space

a="name\nmobile\tmailid\ncity"
print(a)
name
mobile	mailid
city

b="name:mahesh\nmobileno:6789456236\nmailid:mahesh45@gmail.com\tcity:vij"
print(b)
name:mahesh
mobileno:6789456236
mailid:mahesh45@gmail.com	city:vij






#replace()

a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'

b="wait wait until you succeed"
b.replace("wait","wait")
'wait wait until you succeed'

c="net traffic analysis"
c.replace("net","network")
'network traffic analysis'



d="wait wait until you succeed"
d.repace("work","work")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    d.repace("work","work")
AttributeError: 'str' object has no attribute 'repace'. Did you mean: 'replace'?
d.repalce("wait","work")
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    d.repalce("wait","work")
AttributeError: 'str' object has no attribute 'repalce'. Did you mean: 'replace'?
d.replace("wait","work")
'work work until you succeed'





#upper()

a="code"

a.upper()
'CODE'

#lower()

b="PYTHON"
B.lower()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    B.lower()
NameError: name 'B' is not defined. Did you mean: 'b'?
b.lower()
'python'



c="mahesh"
c[0].upper()
'M'

c.captitalize()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    c.captitalize()
AttributeError: 'str' object has no attribute 'captitalize'. Did you mean: 'capitalize'?
c.capitalize()
'Mahesh'


d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'




#isupper, #islower,#isalpha,#isdigit,#isstart,isend()


a="python"

a.isupper()
False

a.islower()
True
a.isalpha()
True

b="python course"
b.isalpha()
False
b.isdigit()
False

c=56789
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c="56789"
c.isdigit()
True

e="codegnan"
e.startswith("c")
True
e.endswith("n")
True

e.endswith("k")
False




#alnum

a="apple"
a.isnum()
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    a.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
a.isalnum()
True


b="apple2"
b.isalnum()
True




#strip()
#lstrip(), rstrip()

a="       mahesh       "
a.strip()
'mahesh'

a.lstrip()
'mahesh       '

a.rstrip()
'       mahesh'



#split()

a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']

b="i love python"
b.split()
['i', 'love', 'python']


#join()

a="python","java","c"
"".join(a)
'pythonjavac'
" ".join(a)
'python java c'

b="cyber security","malware"
"".join()
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    "".join()
TypeError: str.join() takes exactly one argument (0 given)
"".join(b)
'cyber securitymalware'
" ".join(b)
'cyber security malware'



#concatenation()

a="cyber"
b="security"
print(a+b)
cybersecurity


c="code"
d="gnan"
print(c+d)
codegnan

a="python course"
b="at codegnan"
print(a+b)
python courseat codegnan


c="python"
d="course:
SyntaxError: incomplete input
d="course"
print(c+d)
pythoncourse





fname="mahesh"
lname="g"
print(fname+" "lname)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(fname+lname)
maheshg


print(fname+" "+lname)
mahesh g
print(fname.title()+" "lname.title())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(fname.title()+" "+lname.title())
Mahesh G

print((fname+" "lname).title())
SyntaxError: invalid syntax. Perhaps you forgot a comma?



#formatting()


a=4
b=8
print(a+b)
12


print("the sum is",a+b)
the sum is 12


print("the sum is",a+b)
the sum is 12

x="mahesh"
y="g"
print("full name is",x+y)
full name is maheshg


print("full name is",(x+" "+y).title())
full name is Mahesh G

city="vja"
print(city)
vja
>>> 
>>> print("city is",city)
city is vja
>>> 
>>> 
>>> 
>>> #format method()
>>> 
>>> a="motu"
>>> b="patlu"
>>> 
>>> print("hello",a+b)
hello motupatlu
>>> 
>>> 
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> 
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> 
>>> print("hello {} hello {}".format(a,b).title())
Hello Motu Hello Patlu
>>> 

>>> 
>>> #formatting string
>>> 
>>> a="tom"
>>> b="henry"
>>> print(f'hello {a}{b}")
...       
SyntaxError: incomplete input
>>> print(f"hello {a}{b}")
...       
hello tomhenry
>>> 
>>> print(f"hello {a} {b}")
...       
hello tom henry
>>> print(f"hello {a} hello {b}".title())
...       
Hello Tom Hello Henry
>>> 
