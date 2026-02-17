Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Silicing

a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'


a="simple is better than complex"
a[:15]
'simple is bette'
a[9:15]
' bette'
a[9:16]
' better'
a[22:29]
'complex'
a[0:6]
'simple'


a="beautiful is better than ugly"

a[0:9]
'beautiful'
a[13:19]
'better'
a[25:29]
'ugly'



#negativesilicing


a="work hard until you succed"

b="vijayawada is a royal city"



a[-26:-21]
'work '
a[-26:-22]
'work'
a[-16:-12]
'unti'
a[-16:-11]
'until'
a[-20:-16]
'ard '
a[-21:-17]
'hard'

a[-10:-7]
'you'

a[-7:-1]
' succe'
a[-7:0]
''

a[-7:0]
''
a[-7:-0]
''
a[-7]
' '
a[-7:]
' succed'

b="vijayawada is a royal city"
b[-10:-5]
'royal'
b[-26:-16]
'vijayawada'
b[-4:]
'city'









#

a="cloud computing"
a[::]
'cloud computing'
a[::1]
'cloud computing'
a[::3]
'cucpi'
a[::2]
'codcmuig'
'codcmuig'
'codcmuig'



#striding


a="data science"
a[::4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[::4]
'd e'
a[::2]
'dt cec'
a[::5]
'dsc'
a[::8]
'de'
a[1:8]
'ata sci'
a[5:]
'science'
a[3:9]
'a scie'
a[4:10]
' scien'






a="python course"

a[0:5:2]
'pto'
a[1:8:3]
'yoc'



a[2:12:3]
'tnos'

a[5:12:4]
'nu'
a[1:11:5]
'y '

a[0:9:2]
'pto o'





#negativestriding




a="machine learning"

a[-1:-8:-2]
'gire'

>>> 
>>> 
>>> a[-1:-12:-4]
'gr '
>>> 
>>> a[-2:-16:-5]
'nei'
>>> 
>>> a[-4:-15:-2]
'naleic'
>>> 
>>> 
>>> 
>>> a="pyton course"
>>> a[a1:]
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    a[a1:]
NameError: name 'a1' is not defined. Did you mean: 'a'?
>>> a[-1:]
'e'
>>> a[::1]
'pyton course'
>>> a[::-1]
'esruoc notyp'
>>> a[7:5:2]
''
>>> a[5:7:2]
' '
>>> a="python course"
>>> 
>>> a[1;]
SyntaxError: invalid syntax
>>> a[1:]
'ython course'
>>> a[-1:]
'e'
>>> a[::-1]
'esruoc nohtyp'
>>> a[::1]
'python course'
>>> a[7:5:2]
''
>>> a[5:7:2]
'n'
>>> 
