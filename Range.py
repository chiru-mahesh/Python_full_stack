#range()


#start-stop-step

'''for i in range(10):
    print(i)'''


'''for i in range(5,15):
    print(i)'''



#task

#5,10,15,20,25,30,35,40,45
#2,4,6,8,10,12,14,16,18
#3,6,9,12,15,18,21,24,27



'''for i in range(5,45,5):
    print(i)'''


'''for i in range(2,18,2):
    print(i)'''
       


'''for i in range(3,27,3):
    print(i)'''




'''for i in range(5,45,5):
    print(i,end=",")'''


'''for i in range(2,18,2):
    print(i,end=",")'''
       


'''for i in range(3,27,3):
    print(i,end=",")'''



#task2
#grade code

'''while True:
    marks=int(input("enter a grade"))
    if marks in range(91,101):
        print("grade A")

    elif marks in range(81,91):
        print("grade B")

    elif marks in range(71,81):
        print("grade C")
        
    elif marks in range(50,71):
        print("grade D")
    else:
        print("Fail,study well...")'''



#break


'''a=10
while a<1:
    print(a)'''



'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''



'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)'''



'''for i in range(20):
    print(i)'''


'''for i in range(20):
    if i==11:
        break
    print(i)'''



#continue()

'''a=30
while a>5:
    print(a)
    a=a-1'''



'''a=30
while a>5:
    a=a-1
    print(a)'''


'''a=30
while a>5:
    print(a)
    a=a-1
    if a==15:
        continue'''



'''a=30
while a>5:
    a=a-1
    if a==15:
       continue
    print(a)'''



'''for i in range(25):
    print(i)'''

'''for i in range(25):
    if i==20:
        continue
    print(i)'''


'''a="course"
for i in a:
    if i=="r":
        continue
    print(i)'''




#pass

'''a=30
while a>20:
    print(a)
    a=a-1'''
        

'''a=30
while a>20:
    print(a)
    a=a-1
    if a==15:
        pass'''


'''for i in range(8):
    if i==4:
        pass
    print(i)''''
