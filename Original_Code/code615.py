s_rim = [1,5,10,50,100,500,1000]
rim = {0:"""",
       1:""I"",
       5:""V"",
       10:""X"",
       50:""L"",
       100:""C"",
       500:""D"",
       1000:""M"",
       4:""IV"",
       9:""IX"",
       40:""XL"",
       90:""XC"",
       400:""CD"",
       900:""CM""}
for i in range(len(s_rim)):
    if str(s_rim[i])[0] == ""1"":
        rim[s_rim[i]*2] = rim[s_rim[i]]*2
        rim[s_rim[i]*3] = rim[s_rim[i]]*3
    if str(s_rim[i])[0] == ""5"":
        rim[s_rim[i]+s_rim[i-1]*1] = rim[s_rim[i]]+rim[s_rim[i-1]*1]
        rim[s_rim[i]+s_rim[i-1]*2] = rim[s_rim[i]]+rim[s_rim[i-1]*2]
        rim[s_rim[i]+s_rim[i-1]*3] = rim[s_rim[i]]+rim[s_rim[i-1]*3]
d = input()
mn=1
result = """"
for i in range(len(d)):
    result=rim[int(d[(i+1)*(-1)])*mn]+result
    mn*=10
print(result)    