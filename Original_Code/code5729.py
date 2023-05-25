def count_sort(a):
  a1 = []
  b = [0 for i in range(10)]
  for j in range(len(a)):
    a1.append(0)
    b[a[j]-1] = b[a[j]-1]+1
  for i in range(1, len(b)):
    b[i] = b[i] + b[i-1]
  for j in range(len(a)-1, -1, -1):
    a1[b[a[j]-1]-1] = a[j]
    b[a[j]-1] = b[a[j]-1] - 1
  return a1

n = int(input())
a = [int(i) for i in input().split()]
print(*count_sort(a))




 