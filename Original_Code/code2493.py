# codding: utf8
n = int(input ())
b=""программист""
e = ""!""

#for n in range (1001) :

if (n==0) : e=""ов"" ; e1=""  0""  
elif (n==1) : e="""" ; e1=""  1""  
elif (1<n<5) : e=""а"" ; e1=""..2-4""  
elif (4<n<21) : e=""ов"" ; e1=""..5-20""  
elif (110<n<121)or (210<n<221)or (310<n<321)or (410<n<421)or (510<n<521)or (610<n<621)or (710<n<721)or (810<n<821) or (910<n<921): e=""ов"" ; e1=""..111..120""  
elif (n%10==1) : e="""" ; e1=""..1""     
elif (n%10==0) : e=""ов"" ; e1=""..0""
elif (n%10==9) : e=""ов"" ; e1=""..9"" 
elif (n%10==8) : e=""ов"" ; e1=""..8"" 
elif (n%10==7) : e=""ов"" ; e1=""..7"" 
elif (n%10==6) : e=""ов"" ; e1=""..6"" 
elif (n%10==5) : e=""ов"" ; e1=""..5"" 
elif (n%10==4) : e=""а"" ; e1=""..4""
elif (n%10==3) : e=""а"" ; e1=""..3"" 
elif (n%10==2) : e=""а"" ; e1=""..2"" 
#print (str(n)+"" ""+b+e+e1)
print (str(n)+"" ""+b+e)
    
 