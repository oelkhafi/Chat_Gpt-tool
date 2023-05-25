a1=int(input())
a2=int(input())
a3=int(input())
if a1>=a2 and a1>=a3 :
    if a2>=a3:
        print (a1)
        print (a3)
        print (a2)
    elif a3>=a2:
        print (a1)
        print (a2)
        print (a3)

elif a2>=a3 and a2>=a1:
    if a1>=a3:
        print (a2)
        print (a3)
        print (a1)
    elif a3>=a1:
        print (a2)
        print (a1)
        print (a3)    

elif a3>=a1 and a3>=a2:
    if a1>=a2:
        print (a3)
        print (a2)
        print (a1)
    elif a2>=a1:
        print (a3)
        print (a1)
        print (a2)




 