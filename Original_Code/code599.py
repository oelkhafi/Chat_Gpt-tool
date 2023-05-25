# put your python code here
# -*- coding: utf-8 -*-
import copy

molodes =3
tak_sebe = 1
komand = {}
result = [0,0,0,0]
for i in range(int(input())):
    k1, r1, k2, r2 = input().split("";"")
    r1, r2 = int(r1), int(r2)
    if k1 not in komand:
        komand[k1] = copy.deepcopy(result)
    if k2 not in komand:
        komand[k2] = copy.deepcopy(result)
    if r1>r2:
        komand[k1][0] +=1
        komand[k2][0] +=1
        komand[k1][1] +=1
        komand[k2][3] +=1
    elif r2>r1:
        komand[k1][0] +=1
        komand[k2][0] +=1
        komand[k2][1] +=1
        komand[k1][3] +=1
    else:
        komand[k1][0] +=1
        komand[k2][0] +=1
        komand[k1][2] +=1
        komand[k2][2] +=1
for i in komand:
    print(""{}:{} {} {} {} {}"".format(i,komand[i][0],komand[i][1],komand[i][2],komand[i][3],komand[i][1]*molodes+komand[i][2]*tak_sebe)) 