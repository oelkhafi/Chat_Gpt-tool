W, n = map(int, input().split())
w = [int(i) for i in input().split()]


def find(W, w, c):
  d = [[i for i in range(n+1)] for j in range(W+1)]
  for i in range(W+1):
    d[i][0] = 0
  for i in range(n+1):
    d[0][i] = 0
  for i in range(1, n+1):
    for j in range(1, W+1):
      d[j][i] = d[j][i-1]
      if w[i-1] <= j:
        d[j][i] = max(d[j][i], d[j-w[i-1]][i-1]+c[i-1])
  return d[W][len(c)]

print(find(W, w, w))




 