#File Handling

#write()

'''a=open("mahesh.txt","w")
a.write("codegnan it solutions")
a.close()'''


'''a=open("mahesh.txt","w")
a.write("python")
a.close()'''


#append()

'''a=open("mahesh.txt","a")
a.write("\tpython")
a.close()'''


#run_time_input()

'''a=open("mahesh.txt","w")
a.write(input("data"))
a.close()'''


'''a=open("mahesh.txt","w")
b=input("data")
a.write(b)
a.close()'''



'''a=open("mahesh.txt","w")
a.write(input("data"))
a.close()'''



#readlines()

'''a=open("mahesh.txt")
print(a.read())  #it will display entire content
print(a.readline()) #it will dispaly  first line
print(a.readlines()) #it will display with \n
print(a.read(7)) #it will display no. of characters'''


#writeline()   # it makes every object side by side

'''a=open("data.txt","w")
b=["python","dsa","java","html","css"]
a.writelines(b)
a.close()'''


'''a=open("data.txt","w")
b=["python","dsa","java","html","css"]
a.writelines("\n".join(b))
a.close()'''


'''a=open("conditions.py")
print(a.read())'''


'''a=open("C:\\Users\\Mahesh\\Downloads\\Python full stack\\range.py")
print(a.read())'''






#error handling


#syntax error --- complie error
#runtime error --- execution time it will happens
#logical error --- error in logic(it cant visible)


#syntax error

'''for i in range(10)
print(i)'''

#runtime error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''


#logical error
'''a=10
b=20
print(a-b)'''


'''a=2
b=5
if a>b:
    print("True")'''


#exception handling


#try --- instructions from which we are expecting the exceptions
#except--- execption is rasied in try block. it will be handle by this block
#else --- optional (no-expection)
#finally --- always it will display


while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends.....")

