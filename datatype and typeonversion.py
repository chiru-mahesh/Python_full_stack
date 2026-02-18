Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#datatypes

a=4
type(a)
<class 'int'>

b=100
type(b)
<class 'int'>

c=8.9
type(c)
<class 'float'>

d='code'
type(d)
<class 'str'>

e="codegnan"
type(e)
<class 'str'>

f='''python'''
type(f)
<class 'str'>

g="p"
type(g)
<class 'str'>

x=5+9j
type(x)
<class 'complex'>

y=6j+7
type(y)
<class 'complex'>

z=6j
type(z)
<class 'complex'>

b="j"
type(b)
<class 'str'>

a=True
type(a)
<class 'bool'>

b=False
type(b)
<class 'bool'>


#datatypeconversion

#typeconversion

#int()
int(7)
7
int(7.8)
7
int("mahesh")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    int("mahesh")
ValueError: invalid literal for int() with base 10: 'mahesh'

int(7+9j)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(7+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#float()
float(3)
3.0
float(7.8)
7.8
float("hi")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(6+9j)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'

float(True)
1.0
float(False)
0.0


#str
>>> str(7)
'7'
>>> str(8.9)
'8.9'
>>> str("hello")
'hello'
>>> str(6+9j)
'(6+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> 
>>> #complex
>>> complex(2)
(2+0j)
>>> complex(6.7)
(6.7+0j)
>>> complex("python")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
>>> complex(4+9j)
(4+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> 
>>> #bool
>>> bool(7)
True
>>> bool(5.6)
True
>>> bool("hi")
True
>>> bool(6+8j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> 
