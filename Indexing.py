Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#indexing

a="i am in classs"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'

a[5]+a[6]
'in'


a[1]+a[4]+a[7]
'   '


a="i love python"

a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'python'

a[2]+a[3]+a[4]+a[5]
'love'

>>> 
>>> a="time is very precious"
>>> 
>>> a[14]
'r'
>>> a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'precious'
>>> 
>>> a[8]+a[9]+a[10]+[11]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a[8]+a[9]+a[10]+[11]
TypeError: can only concatenate str (not "list") to str
>>> a[8]+a[9]+a[10]+a[11]
'very'
>>> 
>>> 
>>> a[5]+a[6]
'is'
>>> 
>>> 
>>> #NegativeIndexing
>>> 
>>> a="word hard"
>>> 
>>> a[-1]+a[-2]+a[-3]+a[-4]
'drah'
>>> 
>>> 
a
>>> a[-4]+a[-3]+a[-2]+a[-1]
'hard'
>>> 
>>> a[-9]+a[-8]+a[-7]+a[-6]
'word'
>>> 
>>> 
>>> a=" iam learning python"
>>> 
>>> a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'learn'
>>> 
>>> a[-18]+a[-19]
'ai'
>>> a[-19]+a[18]
'io'
>>> 
a[-6]+a[-7]+a[-8]+a[-9]+a[-10]
'p gni'
