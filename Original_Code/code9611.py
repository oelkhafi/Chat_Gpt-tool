# put your python code here
n = int(input())

lines = []
cut = []
rightPoints = []
points = []

while n != 0:
    a, b = map(int, input().split())
    lines += [[a, b]]
    n -= 1
    
lines.sort()

for i in range(len(lines)-1):
    if lines[i][1] >= lines[i+1][0]:
        a = lines[i + 1][0]
        b = min(lines[i][1], lines[i+1][1])
        lines.remove(lines[i+1])
        lines.remove(lines[i])
        lines.insert(i,[])
        lines.insert(i+1,[a,b])
for x in lines:
    if x != []:
        cut += [x]

print(len(cut))
for y in cut:
    print(y[1], end=' ') 