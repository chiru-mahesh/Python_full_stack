#variable length arguments:
#variable length argument are automatically store in tuple and we use * arguments.....


'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
d=[5,6,7,8,9,10]
check(d)
e={3,4,5,6,7}
check(*e)
f={"name":"mahesh","city":"vij"}
check(*f)'''



'''def check1(*a):
    d=2 #creating a variable
    print(a)
    print(type(a))
    for i in a:
          if type(i) in (int,float):
               d=d+i
               print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,3.5,6.2,4.3)
check1(1,3,5,6.2,3.2,"mahesh")'''





#kwargs(**)

'''def details(**a):
    print(a)
    print(type(a))
details()
d={"idnos":[10,20,30],
   "names":["somanath","aditya","mahesh"],
   "status":["P","A","P"]}
details(**d)'''





'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys() :
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"idnos":[10,20,30],
   "names":["somanath","aditya","mahesh"],
   "status":["P","A","P"]}
details(**d)'''




#both*&** uasge(try)

'''def check1(*a,**b):
    print(a)
    print(type(a))
    print(b)
    print(type(b))
check1()
check1(2,3,4,5,6,7,8,9,10)
for i in b:
    print(b)
check1()
b={"name":"mahesh","month":3}
check1(**b)'''


'''def splitbill():
    a=int(input("enter the total no. of friends"))
    b=int(input("enter the amount"))
    print("the bill is",b//a)'''


#both * and ** usage

'''def final(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("keys is ",i)
        print("value is",j)
final()
data=(2,3,4,5,2.3,4.5)
final(*data)
details={"names":["surya","jaswanth","naveen"],
         "marks":[60,70,80]}
final(**details)
final(*data,**details)'''




#max,min,sum

'''print(max(2,5,6,29,20,10))

print(min(2,5,6,29,20,10))

a=2,3,4,5,6
print(sum(a))

print(sum([2,3,4,6]))'''



#student data


'''def student():
    
     a=int(input("enter total number of student"))
     b=int(input("enter number of student present"))
     c=int(input("enter number of student absent"))
     print("total number of student")
     print("number of student present")
     print("number of student absent")'''





def student_attendance():
    total_students = int(input("enter total number of students: "))
    absent_students = int(input("enter number of absent students: "))
    
    present_students = total_students - absent_students
    
    print("Total Students:", total_students)
    print("Absent Students:", absent_students)
    print("Present Students:", present_students)
student_attendance()

