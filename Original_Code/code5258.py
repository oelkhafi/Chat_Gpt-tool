arr,k = [],0
arr.append([])
[arr[k].append(i) for i in input().split()]
while True:
    arr.append([])
    k+=1
    [arr[k].append(i) for i in input().split()]
    if arr[k][0]==""end"":
        break
arr,k = arr [: - 1],k
newArr = []
for i in range(0,len(arr)+2):
    newArr.append([])
newArr[0].append("" "")
newArr[len(arr)+1].append("" "")
[newArr[0].append(i) for i in arr[len(arr)-1]]
newArr[0].append("" "")
#err
[newArr[len(arr)-1+2].append(i) for i in arr[0]]
newArr[len(arr)-1+2].append("" "")
for i in range(0,len(arr)):
    newArr[i+1].append(arr[i][len(arr[0])-1])
for i in range(0,len(arr)):
    for j in range(0,len(arr[0])):
        newArr[i+1].append(arr[i][j])
for i in range(0,len(arr)):
    newArr[i+1].append(arr[i][0])
for i in range(1,len(arr)+1):
    for j in range(1,len(arr[0])+1):
        arr[i-1][j-1]=int(newArr[i-1][j])+int(newArr[i][j-1])+int(newArr[i+1][j])+int(newArr[i][j+1])
        print(arr[i-1][j-1],end="" "")
    print() 