a, b = input().split()
n = int(a)
m = int(b)
fild = [[0 for i in range(0, m + 2)] for j in range (0, n + 2)]
data = [list("".""+input()+""."") for _ in range(0, n)]
data.append(list("".""*(m+2)))
data.insert(0,list("".""*(m+2)))
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(1, n+1):
    for j in range(1, m+1):
        mine_cnt = 0
        if data[i][j] == ""*"":
            fild[i][j] = ""*""
            continue
        for k  in range(8):
            if data[i + dy[k]][j + dx[k]] == ""*"":
                mine_cnt += 1
        fild[i][j] = str(mine_cnt)
for i in range(1, n+1):
        print("""".join(fild[i][1:-1]))



 