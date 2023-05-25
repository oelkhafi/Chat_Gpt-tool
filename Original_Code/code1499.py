d={1:[i for i in range(1,int(input())+1)], 2:[],3:[]}
d[1]=d[1][::-1]
e=[]
e+=d[1]
l=len(d[1])
def z(x1,x2):
    d[x2].append(d[x1][len(d[x1])-1])
    d[x1].pop(len(d[x1])-1)
    print(x1,'-', x2)
def c1(l):
    z(1,2)
    z(1,3)
    z(2,3)
def c123(l):
    c23(l)    
def c13(l):
    z(1,2)
    z(3,1)
    z(3,2)    
def c21(l):
    c1(l)     
def c213(l):
    c13(l)    
def c31(l):
    c1(l)
def c321(l):
    z(1,2)
    if d[3][len(d[3])-1]>d[1][len(d[1])-1]: z(1,3)    
    else: z(3,1)
    z(2,3)   
def c23(l):
    z(2,1)
    z(3,1)
    if d[2]!=[]:    
        if d[2][len(d[2])-1]>d[3][len(d[3])-1]: z(3,2)    
        else: z(2,3)
    else: z(2,3)  
def c231(l):
    c1(l)
#------------------------------------------------
def n1(l):
    z(1,3)
    z(1,2)
    z(3,2)
def n100(l):
    z(1,3)    
def n12(l):
    z(1,3)
    z(2,1)
    z(2,3)
def n123(l):
    n23(l)    
def n13(l):
    z(1,2)
    z(3,2)
    if d[3][len(d[3])-1]>d[1][len(d[1])-1]: z(1,3)
    else: z(3,1)
def n132(l):
    n32(l)        
def n213(l): 
    z(1,2)
    z(3,2)
    if d[3]!=[]: 
        if d[1][len(d[1])-1]>d[3][len(d[3])-1]: z(3,1)
        else: z(1,3)
    else: z(1,3)    
def n23(l):
    z(2,1)
    z(3,2)
    z(3,1)        
def n31(l):
    n100(l)        
def n312(l):
    z(2,1)
    if d[3][len(d[3])-1]>d[2][len(d[2])-1]: z(2,3)
    else: z(3,2)
    z(1,3)
def n32(l):
    z(2,1)
    z(2,3)
    z(1,3)   
while d[3]!=e:        
    if l%2==0 and d[1]!=[] and d[2]==[] and d[3]==[]:
        c1(l)
    if d[3]==e: break
    if d[1]!=[] and d[3]!=[]:
        if l%2==0 and d[1][len(d[1])-1]>d[3][len(d[3])-1] and d[2]==[]:
            c13(l)
    if d[1]!=[] and d[2]!=[]:
        if l%2==0 and d[2][len(d[2])-1]>d[1][len(d[1])-1] and d[3]==[]:
            c21(l)
    if d[2]!=[] and d[3]!=[]:
        if l%2==0 and d[2][len(d[2])-1]>d[3][len(d[3])-1] and d[1]==[]:
            c23(l) 
    if l%2==0 and d[3][len(d[3])-1]>d[1][len(d[1])-1] and d[2]==[]:
        c31(l)    
    if d[1]!=[] and d[2]!=[] and d[3]!=[]:
        if l%2==0 and d[3][len(d[3])-1]>d[2][len(d[2])-1] and d[2][len(d[2])-1]>d[1][len(d[1])-1]:
            c321(l)
    if d[1]!=[] and d[2]!=[] and d[3]!=[]:
        if l%2==0 and d[2][len(d[2])-1]>d[1][len(d[1])-1] and d[1][len(d[1])-1]>d[3][len(d[3])-1]:
            c213(l)   
    if d[1]!=[] and d[2]!=[] and d[3]!=[]:   
        if l%2==0 and d[2][len(d[2])-1]>d[3][len(d[3])-1] and d[3][len(d[3])-1]>d[1][len(d[1])-1]:
            c231(l)
    if d[1]!=[] and d[2]!=[] and d[3]!=[]:
        if l%2==0 and d[1][len(d[1])-1]>d[2][len(d[2])-1] and d[2][len(d[2])-1]>d[3][len(d[3])-1]:
            c123(l)
    if l%2!=0:
        if d[1]!=[]:
            if len(d[1])==1 and d[2]==[] and d[3]==[]:
                n100(l)
                break
        if d[2]==[] and d[3]==[]:        
            n1(l)
            
        if d[1]!=[] and d[2]!=[]:
            if d[1][len(d[1])-1]>d[2][len(d[2])-1] and d[3]==[]:
                n12(l)
                    
        if d[1]!=[] and d[3]!=[]:
            if d[1][len(d[1])-1]>d[3][len(d[3])-1] and d[2]==[]:    
                n13(l)
        if d[1]!=[] and d[3]!=[]:
            if d[3][len(d[3])-1]>d[1][len(d[1])-1] and d[2]==[]:    
                n31(l)
                    
        if d[2]!=[] and d[3]!=[]:
            if d[2][len(d[2])-1]>d[3][len(d[3])-1] and d[1]==[]:    
                n23(l)
        if d[2]!=[] and d[3]!=[]:
            if d[3][len(d[3])-1]>d[2][len(d[2])-1] and d[1]==[]:    
                n32(l)
                
        if d[1]!=[] and d[2]!=[] and d[3]!=[]:
            if d[3][len(d[3])-1]>d[1][len(d[1])-1] and d[1][len(d[1])-1]>d[2][len(d[2])-1]:
                n312(l)
        if d[1]!=[] and d[2]!=[] and d[3]!=[]:
            if d[2][len(d[2])-1]>d[1][len(d[1])-1] and d[1][len(d[1])-1]>d[3][len(d[3])-1]:
                n213(l)
        if d[1]!=[] and d[2]!=[] and d[3]!=[]:
            if d[1][len(d[1])-1]>d[3][len(d[3])-1] and d[3][len(d[3])-1]>d[2][len(d[2])-1]:
                n132(l)                
        if d[1]!=[] and d[2]!=[] and d[3]!=[]:
            if d[1][len(d[1])-1]>d[2][len(d[2])-1] and d[2][len(d[2])-1]>d[3][len(d[3])-1]:
                n123(l) 